from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from .models import Profile
from .forms import SignupForm,LoginForm,UserForm
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.contrib.auth.models import User
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





#@login_required
#@transaction.atomic
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = SignupForm(request.POST)
               
        if user_form.is_valid() and profile_form.is_valid():
            	user_form.save()
            	username=user_form.cleaned_data.get('username')
            	password=user_form.cleaned_data.get('password')
            	user=authenticate(username=username,password=password)
            	print(user)
            	#login(request,user)
            	return HttpResponseRedirect('/base')  
    else:
        user_form = UserForm()
        profile_form = SignupForm()
    token = {}
    token.update(csrf(request))
    token['user_form'] = user_form
    token['profile_form']=profile_form
    return render_to_response('primeExchange/signup.html',token)


def login_view(request):
	token={}
	token.update(csrf(request))
	token['form']=LoginForm
	return render_to_response('primeExchange/login.html',token)


def process_login(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=authenticate(username=username,password=password)
	print("username =",username)
	print("password =",password)
	print("auth= ",user)

	if user is not None:
		login(request,user)
		return HttpResponseRedirect('/base')
	else:
		return HttpResponseRedirect('/login')



def logout_view(request):
	role="0"
	if 'role' in request.session:
		role=request.session['role']
		if role=='Prime_Administrator':
			print("hello")
			return render(request,"primeExchange/signup.html",{})
	#print(role)
	#print(role)
	#print(role)
	print("999")
	#logout(request)
	return render(request,"primeExchange/logout.html",{})
	





#@login_required
def base(request):
	role="none"
	if 'role' in request.session:
		role=request.session['role']
		print(role)
	return render(request,"primeExchange/base.html",{'role':role})




