from django.contrib import admin
from .models import Profile
from .forms import SignupForm
# Register your models here.

class  ProfileAdmin(admin.ModelAdmin):

	list_display=["username","first_name","last_name","email","role","mobile","date"]
	form=SignupForm



admin.site.register(Profile,ProfileAdmin)