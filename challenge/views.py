from django.http import HttpResponse
from django.shortcuts import render

from models import Customer, Team

def index(request):
	return HttpResponse("Index page")

def customer(request, customer_id):
	customer = Customer.objects.get(id=customer_id)
	response = "customer name %s" % customer.name
	return HttpResponse(response)

def team(request, team_id):
	team = Team.objects.get(id=team_id)
	customer = team.customer
	response = "team name %s" % team.name
	return HttpResponse(response)