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
django-admin startproject <name-of-project>
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

## <font color="LightGreen">Main Django Files</font>

* manage.py - This is the file that is used to run the application. *Do not modify this file*.
* settings.py - This is the file that is used for all of the settings for a Django project, such as the applications, middleware and templates that will make up the application.
* urls.py - The list of urls / routes that are available and where each one will do.

There are other files but they are less important.

## <font color="LightGreen">Django Applications</font>

Django supports splitting up an application into multiple smaller applications that would account for different functions. For example:

![Django Apps](assets/images/notes/02-django-apps-example.png)

Each app in the example has its own database models, URL routing and templates that are relevant to that application.

Although splitting the project up into separate is not required (you can do everything in one app), it is recommended to split the project up into smaller apps. The main reasons are:

* Performance - If the app gets a heavy load, scaling it out / up will be difficult.
* Permissions - If the project has multiple apps, access to them can be granular. This means only the devs / admins that need access to the app can be given access to it, rather than the entire app.

To create an app, run the following command:

``` shell
python manage.py startapp <name-of-app>
```

A new folder with the name of the app you gave. Inside will be more boilerplate files.

Once the app is created, it needs to be added to the settings.py file (in the INSTALLED_APPS list) in the main project folder.

The format to add the app to the list is folder-name.apps.ProjectsConfig.

## <font color="LightGreen">Django Views and URL's</font>

![Django URL's](assets/images/notes/03-urls-views-01.png)

In the `urls.py` file, there is a list of path patterns that are used to tell the server what to do when a particular part of the site is requested.

The below is from the `urls.py` file. It contains two paths; one for the admin portal (added by default) and one for a *projects* url that was manually added.

``` python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name = "projects")
]
```

The breakdown of the projects path is as follows:

* 'projects/' - The URL to use.
* projects - The name of the function / class / view to use.
* name = 'projects' - An internal name that can be used for reference.

Notice that there is no root URL defined. To add one, create a new path as follows (for example):

``` python
path('', projects, name = "root")
```

To pass dynamic content to a function using the URL, use <> in the part of the URL that will have the content that will change. For example:

``` python
def project(request, key):
    return HttpResponse(f"The key is {key}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/<str:key>/', project, name = "project")
]
```
