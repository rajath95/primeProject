from django.contrib import admin
from .models import Profile,Commodities
from .forms import SignupForm
# Register your models here.

class  ProfileAdmin(admin.ModelAdmin):

	list_display=["username","first_name","last_name","email","role","mobile","date"]
	form=SignupForm



admin.site.register(Profile,ProfileAdmin)

class CommodityAdmin(admin.ModelAdmin):
	list_display=["commodity","price"]


admin.site.register(Commodities,CommodityAdmin)