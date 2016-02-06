from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	dob = models.DateField('Date of Birth')
	active = models.BooleanField(default=True)
	GENDER_MALE = 0
	GENDER_FEMALE = 1
	GENDER_CHOICES = [
		(GENDER_MALE, 'Male'),
		(GENDER_FEMALE, 'Female'),
	]

	gender = models.IntegerField(choices=GENDER_CHOICES)

class HealthData(models.Model):
	date = models.DateField('Date', db_index=True, auto_now_add=True)
	index = models.IntegerField(default=1, db_index=True)
	value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

class Weight(HealthData):
	user = models.ForeignKey(User, related_name='weight')

class PBF(HealthData):
	user = models.ForeignKey(User, related_name='pbf')

class BFM(HealthData):
	user = models.ForeignKey(User, related_name='bfm')

class SMM(HealthData):
	user = models.ForeignKey(User, related_name='smm')