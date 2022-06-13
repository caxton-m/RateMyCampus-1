from django.shortcuts import render, redirect
from .models import Restaurant
from .models import Review
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, Restaurants


# Create your views here.

# Function to handle the search functionality
def search_venues(request):

    # If the search button is pressed
    if request.method == "POST":

        # Get the search value and filter the restaurants database based on the search
        searched = request.POST['searched']
        venues = Restaurant.objects.filter(name__contains=searched)

        # Return the results page and pass through the data
        return render(request, "main/results.html", {'searched': searched, 'venues': venues})
    else:
        return render(request, "main/results.html", {})


# Function to return the home page
def home(response):
    return render(response, "main/home.html", {})


# Function to handle the registration page
def signup(response):

    # If the submit button on the registration form is pressed
    if response.method == 'POST':
        form = RegisterForm(response.POST)

        # Store the forms data and save it to the database
        if form.is_valid():
            form.save()
            # Route to the users table
            return redirect('/users')
    else:
        form = RegisterForm()

    return render(response, "registration/signup.html", {"form": form})


# Function to display the users table
def users(response):
    return render(response, "main/users.html", {"users": User.objects.all()})


# Ensure the user must be logged in to leave a review
@login_required
def leaveReview(request):

    # Get the restaurant list and convert to a list
    restaurant_list = list(Restaurant.objects.all())
    options = [r for r in restaurant_list]

    # If the submit button is pressed
    if request.method == 'POST':

        # Get the data from the form
        rest = request.POST.get('review-restaurant', 'ERROR')
        rating = request.POST.get('review-rating', 'ERROR')
        text = request.POST.get('review-text', 'ERROR')
        created_by = request.user

        # Get the restaurant
        rest = Restaurant.objects.filter(name__contains=rest)[0]

        # Create, store, and save the values for a new review
        r = Review()
        r.restaurant = rest
        r.created_by = created_by
        r.rating = rating
        r.text = text
        r.save()

        # Update restaurant rating average
        reviews = Review.objects.filter(restaurant__name__exact=rest.name)
        average = reviews.aggregate(Avg('rating'))
        rest.rating = round(average['rating__avg'], 2)
        rest.save()

    # Route to the leave a review page again
    return render(request, "main/leaveReview.html", {"options": options})


# Function to handle explore Reviews page
def readReview(response):

    # Get the restaurant list with names and ids
    restaurant_list = list(Restaurant.objects.all())
    options = [r.name for r in restaurant_list]
    rest_id = [l.id for l in restaurant_list]

    # If the submit button is pressed
    if response.method == 'POST':

        # Save and pass through the search and filtered reviews
        searched = response.POST.get('review_search', 'ERROR')
        filtered = Review.objects.filter(restaurant__name__contains=searched)
        return render(response, "main/readReview.html", {"options": options, "reviews": filtered})

    else:
        return render(response, "main/readReview.html", {"options": options})


# Function to handle the add a restaurant form
def restaurants(response):

    # If the submit button was pressed
    if response.method == 'POST':
        form = Restaurants(response.POST)

        # If the form is valid
        if form.is_valid():

            # Create a new restaurant, populate the fields, and save it to the database
            r = Restaurant()
            r.name = form.cleaned_data["name"]
            r.address = form.cleaned_data["address"]
            r.rating = form.cleaned_data["rating"]
            r.food_type = form.cleaned_data["review"]
            r.save()

        # Redirect to the restaurants table
        return redirect('/view_restaurants/')

    else:
        form = Restaurants()
    return render(response, "main/restaurants.html", {"form": form})


# Function to display the restaurants table
def view_restaurants(response):
    return render(response, "main/view_restaurants.html", {"restaurants": Restaurant.objects.all()})




