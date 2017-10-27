from django.contrib.auth.models import User
from .models import Profile 
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth import login,authenticate
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
    def clean(self,*args,**kwargs):
    	username=self.cleaned_data.get("username")
    	password=self.cleaned_data.get("password")
    	
    	if username and password:    		
	    	user=authenticate(username=username,password=password)
	    	if not user:
	    		raise forms.ValidationError("Invalid username or password")
	    	if not user.check_password(password):
	    		raise forms.ValidationError("Incorrect password")	
	    	if not user.is_active:
	    		raise forms.ValidationError("This user is no longer active")
    	return super(LoginForm,self).clean(*args,**kwargs)

class SignupForm(forms.ModelForm) :

	#widget=forms.Select(choices=ROLES)
	#postal_address=forms.TextField(max_length=100,blank=True)
	#userID is taken from email
	#office_contact=fomrs
	
	confirm_email=forms.EmailField(label="Confirm Email")
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