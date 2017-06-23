
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class AuthForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username':'Username',
				'first_name':'First_name',
				'last_name':'Last_name',
				'email':'Email',
		} 
		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'first_name': forms.TextInput(attrs={'class':'form-control'}),
			'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
		}
