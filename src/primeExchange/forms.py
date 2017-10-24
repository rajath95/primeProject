from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class SignupForm(UserCreationForm) :
	first_name=forms.CharField(max_length=30,required=False,help_text='Optional.')
	last_name=forms.CharField(max_length=30,required=False)
	email=forms.EmailField(max_length=30)
	
	
	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password1','password2')
