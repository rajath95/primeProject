from django.shortcuts import render,redirect
# Create your views here.
from .models import Profile
from .forms import SignupForm,UserForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
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

@login_required
#@transaction.atomic
def update_profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = SignupForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, ('Your profile was successfully updated!'))
            return render(request,'primeExchange/base.html',{})
        else:
        	pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = SignupForm(instance=request.user.profile)
    return render(request, 'primeExchange/signup.html', {'user_form': user_form,
        'profile_form': profile_form})