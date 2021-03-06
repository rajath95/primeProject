from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from .models import Profile,Commodities
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

def fill_admin_profile(user,pform,uform):
	user.profile.role=pform.cleaned_data.get('role')
	user.profile.username=uform.cleaned_data.get('username')
	user.profile.first_name=pform.cleaned_data.get('first_name')
	user.profile.last_name=pform.cleaned_data.get('last_name')
	user.profile.email=uform.cleaned_data.get('email')
	user.profile.mobile=pform.cleaned_data.get('mobile')
	user.profile.date=pform.cleaned_data.get('date')
	user.save()
	return user
            	


#@login_required
#@transaction.atomic
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = SignupForm(request.POST)
               
        if user_form.is_valid() and profile_form.is_valid():
            	user=user_form.save()
            	user=fill_admin_profile(user,profile_form,user_form)
            	name,role,session=create_session(profile_form,user_form,request)
            	return HttpResponseRedirect('/login')  
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
		return HttpResponseRedirect('/base/reports')
	else:
		messages.info(request,"You do not have permission")
		return HttpResponseRedirect('/base')

@login_required()
def analytics(request):
	permission=retrieve_permission(request,module="analytics")
	if permission:
		return HttpResponseRedirect('/base#analytics')
	else:
		messages.info(request,"You do not have permission")
		return HttpResponseRedirect('/base')


	return HttpResponseRedirect('/base#analytics')

@login_required()
def primeadmin(request):
	return HttpResponseRedirect('/base#primeadmin')

def contact(request):
	return HttpResponseRedirect('/base#contact')



def xreport(request):
	
	return render(request,"primeExchange/xreport.html")

def monthly(request):
	commodity_list=Commodities.objects.all()
	m=1
	z=0
	obj_list=[]
	total=0
	if request.method=='GET':
		m=int(request.GET.get('month'))
	print(m)
	for item in commodity_list:
	    month=Commodities.objects.get(commodity=item).date.month
	    print(type(month))
	    if month==m:
	    		z=1
	    		total+=item.price
	    		obj_list.append(item)
	if z:
		return render(request,"primeExchange/xreport.html",{'items':obj_list,'total':total})
	else:
		return render(request,"primeExchange/xreport.html")

	    
	    		