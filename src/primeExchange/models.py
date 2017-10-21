from django.db import models

# Create your models here.



class user_data(models.Model):
	def __str__(self):
		return self.full_name

	full_name=models.CharField(max_length=20)



