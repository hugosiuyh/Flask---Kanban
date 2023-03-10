# Kanban board

## Description

A Kanban board is a simple task management tool. Every task that you add can
be in one of three states:

1. To do
2. Doing
3. Done

Your assignment is to write a Flask application which provides the functionality
associated with a Kanban board. This includes:

1. Creating a new task
2. Moving tasks to different states
3. Deleting tasks

Please find a few example Kanban board websites and use them so that you have a
clear idea of what is needed. Note that the professional versions look much
nicer and have many more bells and whistles than are asked for in this
assignment! Your visual design can be very straightforward.

**(Optional)** As an extension, make a personalizable Kanban board. This means
that every user has their own account, and can see only their own tasks.  For
this you will need to create users, and be able to log them in and out.  Each
task will also need to be associated with a particular user.

## Submission

1. Your primary submission must be a PDF listing of your Python code. This will allow your grader to attach feedback to the code in the PDF.
2. Your secondary submission must be a Zip file containing all the code and documentation for your project. This will allow your grader to run your code and interact with the app.
3. Finally, you need to demo your project. Provide a link in your `README.md` file to a screen recording of you using your app and explaining what you are doing. Demo all the features of your project. The screen recording should be at most 5 minutes long but probably more like 2 minutes long in most cases.

## Installation

As part of your submission you must include a Zip file with all the necessary
code and HTML, a `requirements.txt` file, and a `README.md` file. To get your
application to run should only require the following steps:

**macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

**Windows:**
```bash
python3 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 app.py
```

## Testing
The project must also include at least a few appropriate unit tests. These unit tests should be
run using the following command (while in the project’s root directory):

```bash
python3 -m unittest discover
```

## Hints and best practices

* Write a clear README to give an overview of your project, its features, and where the different parts of the code are located.
* Write detailed code comments. The code comments should explain the intent of the different parts of your code.
* Make sure your screen recording is shared/viewable by your grader. [Loom](https://loom.com/) is a great tool that runs in your browser and is free for educational (`.edu`) accounts. (You don't have to use Loom if you prefer something else.)
* Test your code! Unit tests are the best.
* Make sure that the virtual environment `venv` is **not** included in your Zip file. Virtual environments are not portable, and if you installed it on your laptop then it is unlikely to work anywhere else.
