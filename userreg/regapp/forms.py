# accounts/forms.py

from django import forms
from .models import User, UserProfile

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'phone']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
