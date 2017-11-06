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


def create_session(form,request):
	role=form.cleaned_data['role']
	request.session['role']=role
	return role






#@login_required
#@transaction.atomic
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = SignupForm(request.POST)
               
        if user_form.is_valid() and profile_form.is_valid():
            	user=user_form.save()
            	role=create_session(profile_form,request)
            	print(role)
            	return HttpResponseRedirect('/base',{'role':role})  
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
		if user.is_active:
			login(request,user)
			return HttpResponseRedirect('/base')
		else:
			return HttpResponseRedirect('/login')
	else:
		return HttpResponseRedirect('/login')



def logout_view(request):
	role="0"
	logout(request)
	if 'role' in request.session:
		role=request.session['role']
		if role=='Prime_Administrator':
			print("hello")
			return render(request,"primeExchange/signup.html",{})
	
	
	return render(request,"primeExchange/logout.html",{})
	






def base(request):
	role="none"
	if 'role' in request.session:
		role=request.session['role']
		print(role)
	return render(request,"primeExchange/base.html",{'role':role})


@login_required()
def testimonial(request):
	return HttpResponseRedirect('/base#testimonial')

@login_required()
def reports(request):
	return HttpResponseRedirect('/base#reports')

@login_required()
def analytics(request):
	return HttpResponseRedirect('/base#analytics')

@login_required()
def primeadmin(request):
	return HttpResponseRedirect('/base#primeadmin')

def contact(request):
	return HttpResponseRedirect('/base#contact')