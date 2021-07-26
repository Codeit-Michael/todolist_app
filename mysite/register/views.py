from django.shortcuts import render,redirect

# import for making accounts
from .forms import RegistrationForm

# Create your views here.
def register(response):
	# Making accounts using the built in form
	if response.method == 'POST': # always because we set it
		form = RegistrationForm(response.POST) # make an account from info you enter
		if form.is_valid(): # if the new node satisfies the requirements, save it
			form.save()
		return redirect('/')
	else:
		form = RegistrationForm() 
	return render(response, 'register/register.html', {'form':form})