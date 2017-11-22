from django.contrib.auth.models import User
from .models import Profile,Commodities
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from django.contrib.auth import login,authenticate
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
	username = forms.CharField(label="Username", max_length=30,
							   widget=forms.TextInput(attrs={'class': 'form-control1', 'name': 'Username'}))
	password = forms.CharField(label="Password", max_length=30,
							   widget=forms.PasswordInput(attrs={'class': 'form-control1', 'name': 'password'}))
	def clean_confirm_email(self,*args,**kwargs):
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


class UserForm(forms.ModelForm):


	confirm_email=forms.EmailField(label="Confirm Email",widget=forms.TextInput())
	class Meta:
		model=User
		fields=('username','email','confirm_email','password')
		widgets = {
		'password': forms.PasswordInput(),

		}


	def clean(self):
		cleaned_data=super(UserForm,self).clean()
		p=cleaned_data.get('confirm_email')
		#cleaned_email=super(UserForm,self).clean()
		u=cleaned_data.get('email')
		if p!=u:
			raise forms.ValidationError("Email should be same")

		return cleaned_data

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
        #user.first_name = self.cleaned_data['first_name']
        #user.last_name = self.cleaned_data['last_name']

		#user.refresh_from_db()

		user.email = self.cleaned_data['email']
		password=self.cleaned_data['password']
		user.set_password(password)
		user.is_active=False

		if commit:
			user.save()

		return user


class SignupForm(forms.ModelForm) :

	#widget=forms.Select(choices=ROLES)
	#postal_address=forms.TextField(max_length=100,blank=True)
	#userID is taken from email
	#office_contact=fomrs

	#captcha = CaptchaField()
	class Meta:
		model=Profile
		fields=('first_name','last_name','role','office_contact','mobile','date')


class CommoditiesForm(forms.ModelForm):

	class Meta:
		model=Commodities
		fields=("commodity","price","date")

	def save(self,commit=True):
		com=super(CommoditiesForm,self).save(commit=False)
		com.commodity=self.cleaned_data['commodity']
		com.price=self.cleaned_data['price']
		com.date=self.cleaned_data['date']

		if commit:
			com.save()

		return com
