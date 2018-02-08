from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from .models import Profile,Commodities,doctorMaster,SMSlookup,HospitalRevenue
from .forms import SignupForm,LoginForm,UserForm,CommoditiesForm,DoctorForm,SMSForm
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.template import RequestContext
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect,csrf_exempt
import json
from rest_framework import serializers


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
		month=Commodities.objects.filter(commodity=item)
		month=month[0].date.month

		print(type(month))
		if month==m:
	    		z=1
	    		total+=item.price
	    		obj_list.append(item)
	if z:
		return render(request,"primeExchange/xreport.html",{'items':obj_list,'total':total})
	else:
		return render(request,"primeExchange/xreport.html")


def tables(request):
	records=BadBillingRecord.objects.all()
	return render(request,"primeExchange/table.html",{"tables":records})

def delete_row(request,id):
	row=get_object_or_404(Commodities,commodity=id)
	data=dict()
	if request.method == 'POST':
		row.delete()
		return HttpResponseRedirect("/base/")
	else:
		row.delete()
		return HttpResponseRedirect("/base/")

def new_row(request):
	if request.method == 'POST':
		form=CommoditiesForm(request.POST)
		if form.is_valid():
			com=form.save()
			return HttpResponseRedirect('/reports/')
	else:
		form=CommoditiesForm()
	token={}
	token.update(csrf(request))
	token['form']=form
	return render_to_response('primeExchange/reports/forms.html',token)

def edit_row(request,id):
	com=get_object_or_404(Commodities,commodity=id)
	if request.method == 'POST':
		com.delete()
		form=CommoditiesForm(request.POST)
		if form.is_valid():
			com=form.save()
			return HttpResponseRedirect('/reports/')
	else:
		com_form=CommoditiesForm(instance=com)

	token={}
	token.update(csrf(request))
	token["form"]=com_form
	token["item"]=com
	return render_to_response('primeExchange/reports/edit_forms.html',token)

def dreports(request):

	doc=doctorMaster.objects.all()
	sms=SMSlookup.objects.all()
	token={}
	token["doc_obj"]=doc
	token["sms_obj"]=sms
	return render_to_response("primeExchange/reports/dreports.html",token)


def delete_drow1(request,id):
	row=get_object_or_404(doctorMaster,doctorID=id)
	data=dict()
	if request.method == 'POST':
		row.delete()
		return HttpResponseRedirect("/dreports/")
	else:
		return HttpResponseRedirect("/dreports/")


def delete_drow2(request,id):
	row=get_object_or_404(SMSlookup,recordID=id)
	data=dict()
	if request.method == 'POST':
		row.delete()
		return HttpResponseRedirect("/dreports/")
	else:
		row.delete()
		return HttpResponseRedirect("/dreports/")



def edit_drow1(request,id):
	com=get_object_or_404(doctorMaster,doctorID=id)
	if request.method == 'POST':
		com.delete()
		form=DoctorForm(request.POST)
		if form.is_valid():
			com=form.save()
			return HttpResponseRedirect('/dreports/')
	else:
		com_form=DoctorForm(instance=com)

	token={}
	token.update(csrf(request))
	token["form"]=com_form
	token["item"]=com
	return render_to_response('primeExchange/reports/edit_dforms1.html',token)



def edit_drow2(request,id):
	com=get_object_or_404(SMSlookup,recordID=id)
	if request.method == 'POST':
		com.delete()
		form=SMSForm(request.POST)
		if form.is_valid():
			com=form.save()
			return HttpResponseRedirect('/dreports/')
	else:
		com_form=SMSForm(instance=com)

	token={}
	token.update(csrf(request))
	token["form"]=com_form
	token["item"]=com
	return render_to_response('primeExchange/reports/edit_dforms2.html',token)

def new_drow1(request):
	if request.method == 'POST':
		form=DoctorForm(request.POST)
		if form.is_valid():
			com=form.save()
			return HttpResponseRedirect('/dreports/')
	else:
		form=DoctorForm()
	token={}
	token.update(csrf(request))
	token['form']=form
	return render_to_response('primeExchange/reports/dforms1.html',token)


def new_drow2(request):
	if request.method == 'POST':
		form=SMSForm(request.POST)
		if form.is_valid():
			com=form.save()
			return HttpResponseRedirect('/dreports/')
	else:
		form=SMSForm()
	token={}
	token.update(csrf(request))
	token['form']=form
	return render_to_response('primeExchange/reports/dforms2.html',token)

def display(request,id):
	records=HospitalRevenue.objects.filter(month=id)
	token={}
	token['week1']=records[0]
	token['week2']=records[1]
	token['week3']=records[2]
	token['week4']=records[3]
	return render_to_response('primeExchange/visual.html',token)

@csrf_exempt
def apilogin(request):
	token={}
	token.update(csrf(request))
	token['form']=LoginForm
	return render_to_response('primeExchange/apilogin.html',token)

@csrf_exempt
def api_process_login(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=authenticate(username=username,password=password)


	if user is not None:
		if user.is_active:
			login(request,user)
			name,role,session=update_session(username,request)
			return HttpResponseRedirect('/PrimeAppLoginAPI',{'name':name,'role':role})
		else:
			return HttpResponseRedirect('/login')
	else:
		return HttpResponseRedirect('/login')



@api_view(['GET', 'POST'])
@csrf_exempt
def PrimeAppLoginAPI(request):
	role="none"
	name=""


	api={}
	if 'role' in request.session:
		role=request.session['role']
		name=request.session['username']



	if request.method== 'POST':
		username=request.POST.get('username',)
		password=request.POST.get('password',)
		print("username",username)
		print("password",password)

		u=authenticate(username=username,password=password)
		if u is not None:
			if u.is_active:
				user=User.objects.filter(username=username)
				user=user[0]
				fname=user.profile.first_name
				username=user.username
				api['method']='post'
				api['UserID']=username
				api['key']='good'
				api['userid']=username
				api['"error"']='false'
				api["role"]=role
				api["detail_data"]= {
				"error": "false",
		      	"userid": username,
		      	"pending_day": 23,
		      	"agreed_day": 100,
				"not_agreed_day": 10,
				"pending_monthly": 23,
				"agreed_monthly": 100,
				"not_agreed_monthly": 10,
				"detail_data": [{
					"id":1,
					"uhid":2,
					"first_name":fname,
					"name":3 ,
					"pending": 23,
					"agreed": 222,
					"not_agreed": 2
					},
					{
					"name": fname,
					"pending": 23,
					"agreed": 222,
					"not_agreed": 2
					}
					],
					}
				return Response(api)
			else:
				api["reason"]='inactive'
				return Response(api)
		else:
			api["reason"]='user does not exist'
			return Response(api)


	else:
				return Response(api)

@api_view(['GET','POST'])
def nothing(request):
	import json
	type={}
	if request.method=='GET':
		type['request']='GET'
		return Response(type)
	else:
		print(request.body)
		username=request.POST.get('username')
		password=request.POST.get('password')
		type['request']=username
		return Response(type)
