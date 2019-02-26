from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
	"""docstring for UserRegistrationForm"""
	email = forms.EmailField()

	class Meta:
	 	"""docstring for Meta"""
 		model = User
 		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	"""docstring for UserUpdateForm"""
	email = forms.EmailField()

	class Meta:
	 	"""docstring for Meta"""
 		model = User
 		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	"""docstring for ProfileUpdateForm"""

	class Meta:
	 	"""docstring for Meta"""
 		model = Profile
 		fields = ['image'] 
