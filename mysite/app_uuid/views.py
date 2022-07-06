from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import uuid
import ipaddress
import validators

def verify_ip(ip):
	if validators.url(ip) == True:
		return True

	try:
		ipaddress.ip_address(ip)
	except:
		return False
	return True

def index(request):
    template = loader.get_template('app_uuid/index.html')

    ip = ""
    uuid_ = ""
    error_message = ""
    if request.POST:
    	ip = request.POST['ip'].strip()
    	if verify_ip(ip):
    		uuid_ = uuid.uuid4() 
    	else:
    		error_message = 'Invalid entry.'

    context = {
        'uuid': uuid_,
        'error_message':error_message,
        'ip':ip
    }
    return HttpResponse(template.render(context, request))
