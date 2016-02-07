from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
	customer = models.ForeignKey('challenge.Customer', related_name='users', null=True, blank=True)
	user = models.OneToOneField(User, primary_key=True)
	dob = models.DateField('Date of, Birth', null=True, blank=True)
	active = models.BooleanField(default=True)
	GENDER_MALE = 0
	GENDER_FEMALE = 1
	GENDER_CHOICES = [
		(GENDER_MALE, 'Male'),
		(GENDER_FEMALE, 'Female'),
	]

	gender = models.IntegerField(choices=GENDER_CHOICES, default=0)

	def __str__(self):
		return "%s's profile" % self.user

	def can_manage(self, customer):
		if self.is_superuser or customer.manager.id == self.id:
			return True
		return False

def create_user_profile(sender, instance, created, **kwargs):
	print '1'
	if created:
		print '2'
		profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)

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