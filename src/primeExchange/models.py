from django.db import models

# Create your models here.



class UserData(models.Model):
	def __str__(self):
		return self.full_name

	ROLES=(('Prime_admin','Prime_Administrator'),
	('Hospital_management','Hospital_Management'),
	('Hospital_admin','Hospital_Administrator'),
	)

	first_name=models.CharField(max_length=30,help_text='Optional.')
	last_name=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)
	#role=models.ChoiceField(label="Select Role",choices=ROLES)
	#widget=models.Select(choices=ROLES)
	postal_address=models.TextField(max_length=100,blank=True,null=True)
	#userID is taken from email
	office_contact=models.IntegerField()
	mobile_contact=models.IntegerField()
	



