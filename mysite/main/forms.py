from django import forms

# Main back bone of the form
"""
Django automatically write a js code to render this in browser when its 
passed inside the form tag
"""
class createnewlist(forms.Form):
	name = forms.CharField(label='Name',max_length=200)
	check = forms.BooleanField(required=False)