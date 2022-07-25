from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Icon, Profile, Result


class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ["username", "email"]
