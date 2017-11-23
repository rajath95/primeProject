from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime as dt
from datetime import datetime

# Create your models here.



class Profile(models.Model):

	ROLES=(('Prime_admin','Prime_Administrator'),
	('Hospital_management','Hospital_Management'),
	('Hospital_admin','Hospital_Administrator'),
	)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	username=models.CharField(max_length=10)
	password = models.CharField(max_length=50)
	email=models.EmailField(max_length=30)
	date = models.DateField(("Date"), default=dt.date.today)
	role=models.CharField(default="Prime_Administrator",choices=ROLES,max_length=30)
	mobile= models.CharField(max_length=10)
	office_contact=models.CharField(max_length=10)


	def __str__(self):
		return self.user.username




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





class Commodities(models.Model):
	commodity=models.CharField(max_length=20)
	price=models.IntegerField()
	date=models.DateField(default=dt.date.today)


	def __str__(self):
		return self.commodity

class doctorMaster(models.Model):
	doctorID = models.AutoField(primary_key=True)
	doctorName = models.CharField(max_length=100,null=False)
	doctorDesignation = models.CharField(max_length=100,null=True)
	doctorSpecialization = models.CharField(max_length=100,null=True)
	UpdatedOn = models.DateTimeField(default=timezone.now, null=True)

	def __str__(self):
		return self.doctorID

class serviceCodeMaster(models.Model):

	recordID = models.AutoField(primary_key=True)
	serviceCode = models.CharField(max_length=100,null=False)
	serviceName = models.CharField(max_length=500,null=True)
	serviceCodeCategory = models.CharField(max_length=100,null=True)
	UpdatedOn = models.DateTimeField(default=timezone.now, null=True)
	def __str__(self):
		return self.recordID

class SMSlookup(models.Model):
    recordID = models.AutoField(primary_key=True)
    doctorID = models.IntegerField (null = False)
    doctorName = models.CharField(max_length=100,null=False)
    SMSContact = models.IntegerField (null = False)
    UpdatedOn = models.DateTimeField(default=timezone.now, null=True)
