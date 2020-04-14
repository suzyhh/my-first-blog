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


jango-admin startproject mysite .