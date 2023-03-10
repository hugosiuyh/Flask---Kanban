import unittest
import flask
import os
import tempfile
from flaskr import create_app
from flaskr.db import init_db 
from flask import url_for

class TestApp(unittest.TestCase):

    def setUp(self): 
        self.db_fd, self.db_path = tempfile.mkstemp() 
        self.app = create_app({ 
            'TESTING': True, 
            'DATABASE': self.db_path, 
        }) 
        self.client = self.app.test_client() 
        with self.app.app_context(): 
            init_db() 
            
    def tearDown(self): 
        os.close(self.db_fd) 
        os.unlink(self.db_path) 
        
    def test_redirect_from_home_to_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        
    def test_public_views(self):
        #Test whether it can redirect from index to login
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/auth/login')
        
        #Test whether login page is functional
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200) 
        
        #Test whether register page is functional
        response = self.client.get('/auth/register')
        self.assertEqual(response.status_code, 200) 
    
    def test_register(self):
        with self.app.test_request_context():
            response = self.client.post(url_for('auth.register'), data=dict(
                username='hugo',
                password='hugo',
                first_name = 'hugo'
                ))
        #after submission, it should be redirected immediately 
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/auth/login')
        
        #test whether double submission is possible (should not be)
        with self.app.test_request_context():
            response = self.client.post(url_for('auth.register'), data=dict(
                username='hugo',
                password='hugo',
                first_name = 'hugo'
                ))
        self.assertIn(b'already registered', response.data)
    
    def test_login(self):
        with self.app.test_request_context():
        #register user again
            response = self.client.post(url_for('auth.register'), data=dict(
                username='hugo',
                password='hugo',
                first_name = 'hugo'
                ))
            
        #login with wrong username
            response = self.client.post(url_for('auth.login'), data=dict(
                username= 'gray',
                password= 'testpassword'
            ))
            self.assertIn(b'Incorrect username', response.data)
            
        #login with wrong password
            response = self.client.post(url_for('auth.login'), data=dict(
                username= 'hugo',
                password= 'wrong_password'
            ))
            self.assertIn(b'Incorrect password', response.data)
            
        #login redirects to main page
            response = self.client.post(url_for('auth.login'), data=dict(
                username= 'hugo',
                password= 'hugo'
            ))
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.headers['Location'], '/main')

    def test_logout(self):
        with self.app.test_request_context():
        #register and sign-in
            response = self.client.post(url_for('auth.register'), data=dict(
                    username='hugo',
                    password='hugo',
                    first_name = 'hugo'
                    ))
            response = self.client.post(url_for('auth.login'), data=dict(
                    username= 'hugo',
                    password= 'hugo'
                ))
            
        #logout!
            response = self.client.get('/auth/logout')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.headers['Location'], '/auth/login')

    def test_task(self):
        with self.app.test_request_context():
        #register and sign-in
            self.client.post(url_for('auth.register'), data=dict(
                    username='chloe',
                    password='hugo',
                    first_name = 'hugo'
                    ))
            self.client.post(url_for('auth.login'), data=dict(
                    username= 'chloe',
                    password= 'hugo'
                ))
        #creating a to-do task
            response = self.client.post('/main/create', data={
                'title': 'Test Task',
                'body': 'This is a test task',
                'section': 'to_do',}, follow_redirects=True)
            self.assertIn(b'Test Task', response.data)
            self.assertEqual(response.status_code, 200)
        
        #update a to-do task
            response = self.client.post('/main/update/1', data={
                'title': 'Updated Task',
                'body': 'update!',
                'section': 'in_progress',}, follow_redirects=True)
            
            #make sure it is updated 
            self.assertIn(b'Updated Task', response.data)
            self.assertNotIn(b'Test Task', response.data) 
            self.assertIn(b'update!', response.data)
            self.assertEqual(response.status_code, 200)
        
        #delete task - check whether it is in response data or not
            response = self.client.post('/main/delete/1', follow_redirects=True)
            self.assertNotIn(b'update task', response.data)
            self.assertEqual(response.status_code, 200)
        
        
            
        
        

        
        
        #Test whether it is in the database
        
        #Test whether it is redirected to login page
        # self.assertIn(b'<h1>Register</h1>', response.data)
        # self.assertIn(b'<form method="POST">', response.data)
        # self.assertIn(b'<input name="username" id="username" required>', response.data)
        # self.assertIn(b'<input name="password" id="password" required>', response.data)
        
# def test_login(self):
        
#     def test_home_page(self):
#         response = self.app.get('/main')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'Welcome to my app!', response.data)

# #follow redirect through 
#     def test_login(self):
#         response = self.app.post('/login', data=dict(
#             username='user',
#             password='pass'
#         ), follow_redirects=True)
#         self.assertEqual(flask.session['username'], 'user')

if __name__ == '__main__':
    unittest.main()