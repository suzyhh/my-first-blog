# Code for the Django Girls tutorial

cd Documents/STP

# Make the directory for the tutorial
mkdir djangogirls
cd djangogirls

# Set up python 3 virtual environment called djenv
python3.6 -mvenv djenv
# Enter djenv
source djenv/bin/activate
# Make sure the pip installer is up to date
python -m pip install --upgrade pip
# Install Django 2.2.4 using the requirements text file
# Django~=2.2.4
pip install -r requirements.txt

# Make a PythonAnywhere account
# Username: suzyh
# Create a PythonAnywhere API token
# Account > API Token > Create a new API Token

# Create the Django project
django-admin startproject mysite .

# Now working in mysite/settings.py
# Amend
TIME_ZONE = 'Europe/London'
# Append file
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Amend
# 
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

# Working in the console, let's add a database
python manage.py migrate

# Now start the web server
python manage.py runserver

# To check the browser, navigate to http://127.0.0.1:8000/

# Create a separate application inside the project for the blog
python manage.py startapp blog
# Then amend mysite/settings.py by adding 'blog.apps.BlogConfig' to INSTALLED_APPS
# Now follow the tutorial for creating an ohject for the blog post in models.py
# Now add the model to the database and let Django know we made some changes
python manage.py makemigrations blog

# This prepared a migration file that we can now apply to our database
python manage.py migrate blog

# Now we have modeled the Posts, we can add, edit or delete
# Uses Django admin
# Open blog/admin.py and amend with admin.site.register(Post) to register the Post model
# Now run the web server
python manage.py runserver
# Navigate to http://127.0.0.1:8000/admin
# It is asking for user credentials. Create a super user to control the whole site
python manage.py createsuperuser
# suzy, Wobble101

# Now to set up a git repository
git init

git config --global user.name "suzyhh"
git config --global user.email suzyhocking@gmail.com
