from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create a registration form and set the field types
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


# Create a login form and set the field types
class Login(forms.Form):
    email = forms.CharField(label='Email', max_length=50)
    password = forms.CharField(label='Password', max_length=50)


# Create a restaurant form and set the field types
class Restaurants(forms.Form):
    name = forms.CharField(label='Restaurant Name', max_length=50)
    address = forms.CharField(label='Restaurant Address', max_length=50)
    rating = forms.CharField(label='Rating', max_length=50)
    food_type = forms.CharField(label='Food Type', max_length=50)
