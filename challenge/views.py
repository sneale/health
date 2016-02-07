from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from models import Customer, Team

def index(request):
	template = loader.get_template('dashboard.html')
	print request.user
	context = {}
	return HttpResponse(template.render(context, request))

def customer(request, customer_id):
	customer = Customer.objects.get(id=customer_id)
	response = "customer name %s" % customer.name
	return HttpResponse(response)

def team(request, team_id):
	team = Team.objects.get(id=team_id)
	customer = team.customer
	response = "team name %s" % team.name
	return HttpResponse(response)