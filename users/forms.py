from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):  # inherits from user creation form
    email = forms.EmailField()

    class Meta:
        model = User  # because we want our form to interact with User table
        # fields which we want to displayed in our form
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):  # inherits from user creation form
    email = forms.EmailField()

    class Meta:
        model = User  # because we want our form to interact with User table
        # fields which we want to update in our form
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
