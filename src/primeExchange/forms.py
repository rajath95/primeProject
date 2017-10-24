from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class SignupForm(UserCreationForm) :
	ROLES=(('Prime_admin','Prime_Administrator'),
	('Hospital_management','Hospital_Management'),
	('Hospital_admin','Hospital_Administrator'),
	)
	first_name=forms.CharField(max_length=30,required=False,help_text='Optional.')
	last_name=forms.CharField(max_length=30,required=False)
	email=forms.EmailField(max_length=30)
	role=forms.ChoiceField(label="Select Role",choices=ROLES)
	#widget=forms.Select(choices=ROLES)
	#postal_address=forms.TextField(max_length=100,blank=True)
	#userID is taken from email
	#office_contact=fomrs
	
	class Meta:
		model=User
		fields=('first_name','last_name','email','password1','password2','role')
