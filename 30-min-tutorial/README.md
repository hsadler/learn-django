# Very basic Django example

## Requirements

- python 3
- virtualenv

## Setup

Create a python virtual env and install django
```sh
virtualenv venv
source venv/bin/activate
pip install django
```

Start a Django project
```sh
django-admin startproject <project_name>
```

Rename the "dj30" top-level dir to "src"
```sh
mv dj30/ src/
```

Initialize Django->Sqlite
```sh
python src/manage.py migrate
```

## Development

Create a new Django app
```sh
python src/manage.py startapp <app_name>
```

Create an admin user
```sh
python src/manage.py createsuperuser
```

Manage which apps are used by the project via the `settings.py` file.

Manage request routing in the `urls.py` file

Manage models available on the `/admin` page in the `admin.py` file

Example of models file: [here](https://github.com/hsadler/learn-django/blob/main/30-min-tutorial/src/posts/models.py)

Example of views file: [here](https://github.com/hsadler/learn-django/blob/main/30-min-tutorial/src/posts/views.py)

Example of embedded python template: [here](https://github.com/hsadler/learn-django/blob/main/30-min-tutorial/src/posts/templates/posts/index.html)

Refer to the Makefile for other common Django CLI commands.
