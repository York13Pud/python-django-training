# <font color="Magenta">Django Notes</font>

## <font color="LightGreen">What is Django?</font>

Django is a web backend framework that uses python.

Django REST framework is used to create API's, which can be used with other parts of Django or on it's own.

It uses the MVT (Model, View and Template) design pattern.

![MVT](assets/images/notes/01-mvt.png)

* Model: The data layer that is usually a database.
* View: This is the logical layer that does the processing of the request and then the returning of what the user requested.
* Template: A template is the HTML (or other format) that you want to send back to the user.

## <font color="LightGreen">Setting up Django</font>

First, setup a virtual environment in a folder where you intend to store the project:

``` python
python3 -m venv venv
```

Once the virtual environment is created, activate it:

``` python
source ./venv/bin/activate
```

To exit out of the virtual environment, run `deactivate`.

Once the virtual environment is activated, install django:

``` python
# --- install the latest version:
pip install django

# --- or to install a specific version:
pip install django==3.2.4
```

## <font color="LightGreen">Creating a Django Project</font>

To create a django project, use the `django-admin` command with the `startproject` option:

``` python
django-admin startprogect <name-of-project>
```

This will create a new folder matching the name of the project provided that will have the boilerplate files for a new Django project.

Once the project has been created, the next step is to test that that server will run. To do this, do the following:

``` shell
# go to the folder with the project files in:
cd name-of-project

# Next, run the server:
python manage.py runserver
```

If the server runs, the output will show the IP address and port that the server is running on. Using that, it will take you to the default page for Django.
