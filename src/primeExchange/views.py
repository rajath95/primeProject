from django.shortcuts import render,redirect
# Create your views here.
from .models import Profile
from .forms import SignupForm,LoginForm,UserForm
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
import json

@api_view()
def primeDataExchangeAPI(request):
	import json
	api_response = {}

	if 'jsonBillingData' in request.GET:
		inputJSONstring = request.GET['jsonBillingData']
		inputJSONstring = str(inputJSONstring)
		received_json_data = json.loads(inputJSONstring)
		api_response['UHID'] = received_json_data.get('UHID')
		api_response['AdmissionNumber'] = received_json_data.get('AdmissionNumber')
		api_response['BillingNumber'] = received_json_data.get('BillingNumber')
		api_response['DataExchangeStatus'] = 'SUCCESS'
	return Response(api_response)

@login_required
#@transaction.atomic
def update_profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = SignupForm(request.POST, instance=request.user.profile)
        z=""
        
        if user_form.is_valid() and profile_form.is_valid():
            	user_form.save()
            	profile_form.save()	
            	z= profile_form.cleaned_data['role']
            	print(z)
            	request.session['role']=z
            #messages.success(request, ('Your profile was successfully updated!'))
            	return render(request,'primeExchange/base.html',{'role':z})
        else:
        	pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = SignupForm(instance=request.user.profile)
    return render(request, 'primeExchange/signup.html', {'user_form': user_form,
        'profile_form': profile_form})


def login_view(request):

	form=LoginForm(request.POST or None)
	if form.is_valid():
			username=form.cleaned_data.get("username")
			password=form.cleaned_data.get("password")
			user=authenticate(username=username,password=password)
			person=User.objects.get(username=username)
			guy=Profile.objects.get(user=person)
			print(guy.role)
			request.session['role']=guy.role
			login(request,user)
			return render(request,'primeExchange/base.html',{'role':guy.role,'name':person.username})
	return render(request,"primeExchange/login.html",{"form":form})


def logout_view(request):
	role="0"
	if 'role' in request.session:
		role=request.session['role']
		if role=='Prime_Administrator':
			print("hello")
			return render(request,"primeExchange/signup.html",{})
	print(role)
	print(role)
	print(role)
	print("999")
	#logout(request)
	return render(request,"primeExchange/logout.html",{})
	





@login_required
def base(request):
	

	role="none"
	if 'role' in request.session:
		role=request.session['role']
		print(role)




	return render(request,"primeExchange/base.html",{'role':role})




