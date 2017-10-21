from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
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