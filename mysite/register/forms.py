# import for making accounts
from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class meta:
		model = User
		fields = ['username','email','password1','password2']
		# Remember:Those list items has built in values need to recieve, not just str