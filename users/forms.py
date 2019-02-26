from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
	"""docstring for UserRegistrationForm"""
	email = forms.EmailField()

	class Meta:
	 	"""docstring for Meta"""
 		model = User
 		fields = ['username', 'email', 'password1', 'password2']
