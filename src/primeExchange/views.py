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
from django.contrib import messages
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


def create_session(pform,uform,request):
	role=pform.cleaned_data['role']
	name=uform.cleaned_data['username']
	request.session['username']=name
	request.session['role']=role
	return name,role,request.session

def update_session(username,request):
	user=User.objects.get(username=username)
	user_profile=Profile.objects.get(user=user)
	request.session['username']=user.username
	request.session['role']=user_profile.role
	username=user.username
	role=user_profile.role
	return username,role,request.session

def retrieve_dict():
	mapping={}
	mapping["reports"]=["Hospital_Management","Prime_Administrator"]
	mapping["analytics"]=["Hospital_Management","Prime_Administrator"]
	#mapping[""]=["Hospital_Management","Prime_Administrator"]
	#mapping["reports"]=["Hospital_Management","Prime_Administrator"]

	return mapping

def retrieve_permission(request,module):
	mapping=retrieve_dict()
	if request.session['role'] in mapping[module]:
		return True
	else:
		return False



#@login_required
#@transaction.atomic
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = SignupForm(request.POST)
               
        if user_form.is_valid() and profile_form.is_valid():
            	user=user_form.save()
            	name,role,session=create_session(profile_form,user_form,request)
            	print(name)
            	return HttpResponseRedirect('/base',{'role':role,'name':name})  
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
	

	if user is not None:
		if user.is_active:
			login(request,user)
			name,role,session=update_session(username,request)
			return HttpResponseRedirect('/base',{'name':name,'role':role})
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
	name=""
	if 'role' in request.session:
		role=request.session['role']
		name=request.session['username']
		print(role)
	return render(request,"primeExchange/base.html",{'role':role,'name':name})


@login_required()
def clientaccess(request):

	return HttpResponseRedirect('/base#clientaccess')

@login_required()
def reports(request):
	permission=retrieve_permission(request,module="reports")
	if permission:
		pass
	return HttpResponseRedirect('/base#reports')

@login_required()
def analytics(request):
	permission=retrieve_permission(request,module="analytics")

	return HttpResponseRedirect('/base#analytics')

@login_required()
def primeadmin(request):
	return HttpResponseRedirect('/base#primeadmin')

def contact(request):
	return HttpResponseRedirect('/base#contact')