## Kanban Board

This is a simple flask app that helps users see their tasks and whether it is started, in progress or finished.

## Attribution 
The app is modeled after and reuses code from this Flask tutorial:

*[Flask Tutorial*. (n.d.). Retrieved March 10, 2023](https://flask.palletsprojects.com/en/2.2.x/tutorial/)

## Features 
- User can create tasks, update tasks to put into different sections, and delete tasks
- Users have access to toehri own task boards and managed thorugh username and password login

# Getting Started

Clone the repository:

```bash
git clone 
```

Once you have the repository on your computer, open Terminal, navigate to the main directory (web_app) and run the following:

### macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

### Windows

```bash
python -m venv venv
venv/Scripts/activate.bat
pip3 install -r requirements.txt
python app.py
```

# Testing

The app comes with implemented unit tests covering 95% of the code. To test the app, run the following from the main directory (web_app):

```bash
python3 -m unittest discover
```

To get coverage report, run the following instead: