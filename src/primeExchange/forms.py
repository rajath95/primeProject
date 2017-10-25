from django.contrib.auth.models import User
from .models import Profile 
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class SignupForm(forms.ModelForm) :

	#widget=forms.Select(choices=ROLES)
	#postal_address=forms.TextField(max_length=100,blank=True)
	#userID is taken from email
	#office_contact=fomrs
	
	#password = forms.CharField(max_length=50)
	class Meta:
		model=Profile
		fields=('username','first_name','password','last_name','email','role','office_contact','mobile')
		widgets = {
        'password': forms.PasswordInput(),
    		}

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=('username','email')