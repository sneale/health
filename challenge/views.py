from django import http
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView

from models import Customer, Team

class CustomerList(ListView):
	model = Customer

	def get_context_data(self, **kwargs):
		context = super(CustomerList, self). get_context_data(**kwargs)
		context['object_list'] = Customer.objects.all()
		return context

class TeamList(ListView):
	model = Team

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(TeamList, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		customer = self.kwargs.get('customer_id') or None

		if not customer:
			raise http.Http404

		context['object_list'] = Team.objects.filter(customer__id=customer)
		return context

def index(request):
	template = loader.get_template('dashboard.html')
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