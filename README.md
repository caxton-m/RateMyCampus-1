# RateMyCampus

### How to run

 `python manage.py runserver 8000`
 
### Needed packages
  
  - #### Install the following with `pip install <package_name>`
    - django
    - django-crispy-forms
    - pands
 
## Project Structure
 There are two main folders for this project "CS3203_Project" and "main"
 - CS3203_Project: This is the folder that runs the app. It is created by django, and there is not much to change here.
   - settings.py: This is where the settings for the app are changed
   - urls.py: This is where the route to the main/views.py folder occurs.
 
 - main: This is the main folder for the app. This is where most of the coding will be with the creation of views, models, etc.
   - templates/: folder that holds all of the html files for the website
   - forms.py: File to create the different forms for the website (login, register, add restaurant)
   - models.py: File to create the database models (Restaurant, Review)
   - urls.py: File to set the paths to determine which view is loaded
   - views.py: File to handle the view controller of the site. Handles the GET and POST requests for the site

### ADMIN DASHBOARD LOGIN:
    - username: admin
    - password: TheAeros
