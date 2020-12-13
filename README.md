# Project-Management-System-Django-webapp
## Description
This is a django webapp used to handle projects and tasks. The user can create, update and delete projects and tasks. The project and tasks have their own uniquely addressed detial page where the user can view/edit them.
The web app has 1 app inside django "Project" and has 2 models that are nested "Project_post" and "Tasks" model.
All templates extend the file "base.html" to get the basic styling of the html page. The database used is sqlite database(default) to store, retrieve and update project and task information.

## Setup and run

To setup the project locally follow the instructions:

#### Clone
_**Note**_: _For this you need to install git on your machine. You can download the git tool from [here](https://git-scm.com/downloads)._

- If you have forked the project, run the following command -

  `git clone https://github.com/YOUR_GITHUB_USER_NAME/Project-Management-System-Django-webapp`

  where `YOUR_GITHUB_USER_NAME` is your GitHub handle.

- If you haven't forked the project, run the following command -

  `git clone https://github.com/rishi0904/Project-Management-System-Django-webapp`
  
## Run app
  
Download the latest stable version of Django and install it into you virtual environment.
  
  - Clone this repository
  - Install libraries from requirements.txt
  - Create your superuser(optional)
  - python manage.py runserver
  
### Front_End: 
HTML, CSS, Crispy-Forms, Jinja

### Back_End: 
Python, Django 

### Database 
sqlite3

### External Libraries_used: 
django-crispy-forms 
