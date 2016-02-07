from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	name = models.CharField(db_index=True, max_length=200)
	created_date = models.DateTimeField('created date', db_index=True, auto_now_add=True)
	slug = models.CharField(db_index=True, max_length=200, default='')
	manager = models.ForeignKey(User, related_name='customers_managed', null=True, blank=True)
	
	def __str__(self):
		return self.name

class Team(models.Model):
	created_date = models.DateTimeField('created date', db_index=True, auto_now_add=True)
	customer = models.ForeignKey(Customer, related_name='teams')
	members = models.ManyToManyField(User, related_name='teams')
	name = models.CharField(db_index=True, max_length=200)
	slug = models.CharField(db_index=True, max_length=200, default='')
	latest_index = models.IntegerField(default=1, db_index=True)

	def __str__(self):
		return self.name

	def count(self):
		return self.members.filter(active=True).count()