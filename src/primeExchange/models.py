from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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

