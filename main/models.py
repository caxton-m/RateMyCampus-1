from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# To tell django that this file has been modified:
#       To create migration: python manage.py makemigrations main
#       To push migration to the app: python manage.py migrate


# Restaurant: class to store the details on the restaurants
class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    rating = models.FloatField(null=False)
    food_type = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


# Review: class to store the reviews
class Review(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateField(auto_now=True, null=False)
    text = models.CharField(max_length=400, null=False)
    rating = models.IntegerField(null=False)

    def __str__(self):
        return self.restaurant.name + ': ' + self.text


