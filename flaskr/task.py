from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db
from flaskr.auth import login_required
bp = Blueprint('main', __name__)

@bp.route('/main')
@login_required #user has to be logged in 
def index():
    #put tasks into different status based on their status and user_id
    db = get_db()
    to_do = db.execute('SELECT * FROM task WHERE section="to_do" and user_id = ?', (g.user['id'],)).fetchall()
    in_progress = db.execute('SELECT * FROM task WHERE section="in_progress" and user_id = ?', (g.user['id'],)).fetchall()
    finished = db.execute('SELECT * FROM task WHERE section="finished" and user_id = ?', (g.user['id'],)).fetchall()
    return render_template('content/main.html', to_do=to_do,in_progress=in_progress,finished=finished)

#create a new task
@bp.route('/main/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        section = request.form['section']
        error = None

        if not title:
            error = 'Title is required.'
        if not section:
            error = 'Section is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            #insert into database if there is no error
            db.execute(
                'INSERT INTO task (user_id, title, body, section)'
                ' VALUES (?, ?, ?,?)',
                (g.user['id'],title, body, section)
            )
            db.commit()
            return redirect(url_for('main.index'))

    return render_template('content/create.html')

#retrieve task information from the task table
def get_task(id):
    task = get_db().execute(
        'SELECT id, title, body,section FROM task'
        ' WHERE id = ?',(id,)
    ).fetchone()

    if task is None:
        abort(404, f"Task id {task.id} doesn't exist.")

    return task

#update task 
@bp.route('/main/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    #first retrieve task information so it can be prepopulated into the update page
    task = get_task(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        section = request.form['section'] 
        error = None

        if not title:
            error = 'Title is required.'
        if not section:
            error = 'Section is required.'

        if error is not None:
            flash(error)
        else:
            #update task information based on different info
            db = get_db()
            db.execute(
                'UPDATE task SET user_id = ?,title = ?, body = ?, section =?'
                ' WHERE id = ?',
                (g.user['id'],title, body, section,id)
            )
            db.commit()
            return redirect(url_for('main.index'))
    return render_template('content/update.html', task=task)

#delete task based on id
@bp.route('/main/delete/<int:id>', methods=('POST','GET'))
@login_required
def delete(id):
    get_task(id)
    db = get_db()
    
    db.execute('DELETE FROM task WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('main.index'))