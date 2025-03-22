# Django Project Setup

This guide will help you set up a Django project using the command `python -m django startproject`.

## Prerequisites

Before you start, make sure you have the following installed:
- Python (3.x recommended)
- pip (Python package manager)
- Virtual environment (optional but recommended)
- Django

## Step 1: Install Django

First, install Django using pip:

```bash
pip install django
```
 
## Step 2: Create a Django Project(Optional)

To create a new Django project, run the following command:

```bash
python -m django startproject projectname
```

Replace `projectname` with the desired name of your project.

## Step 3: Navigate to the Project Directory

```bash
cd youtube_manager_app
```

## Step 4: Run the Development Server

To verify that everything is set up correctly, run:

```bash
python manage.py runserver
```

You should see output similar to this:

```
Watching for file changes with StatReloader
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open `http://127.0.0.1:8000/` in your browser to see the default Django welcome page.

## Step 5: Create a Django App (Optional)

To create an app within your Django project, use the following command:

```bash
python manage.py startapp appname
```

Replace `appname` with your desired app name.

## Step 6: Apply Migrations

Before running the project, apply migrations to set up the database:

```bash
python manage.py migrate
```

## Step 7: Create a Superuser (For Admin Panel)

To create an admin user, run:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.

## Step 8: Access the Django Admin Panel

Start the server and go to:

```
http://127.0.0.1:8000/admin/
```

Log in with the superuser credentials you created.

## Conclusion

You have successfully set up a Django project and started the development server! You can now build and customize your application.

