from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from osnow.models import Usuari

def mainpage(request): 
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'OpenShareNow',
		'pagetitle': 'Welcome to the Sobres aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def userpage(request, login):
	try:
		user = Usuari.objects.get(login=login)
	except:
		raise Http404('User not found.')
	#sobres = user.sobre_set.all()
	template = get_template('userpage.html')
	variables = Context({
		'login': login,
		#'sobres': sobres
		})
	output = template.render(variables)
	return HttpResponse(output)
