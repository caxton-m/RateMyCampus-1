from django.urls import path, include
from . import views

# Set the url patterns for the website
urlpatterns = [
    path("", views.home, name="home"),
    path("", include("django.contrib.auth.urls")),
    path("users/", views.users, name="users"),
    path("signup/", views.signup, name="signup"),
    path("leaveReview/", views.leaveReview, name="leaveReview"),
    path("readReview/", views.readReview, name = "readReview"),
    path("add_restaurants/", views.restaurants, name="add-restaurants"),
    path("view_restaurants/", views.view_restaurants, name="view-restaurants"),
    path("results/", views.search_venues, name="search-venues"),
]

