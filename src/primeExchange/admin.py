from django.contrib import admin
from .models import Profile,Commodities,doctorMaster,serviceCodeMaster,SMSlookup
from .forms import SignupForm
# Register your models here.

class  ProfileAdmin(admin.ModelAdmin):

	list_display=["username","first_name","last_name","email","role","mobile","date"]
	form=SignupForm


admin.site.register(Profile,ProfileAdmin)

class CommodityAdmin(admin.ModelAdmin):
	list_display=["commodity","price"]

admin.site.register(Commodities,CommodityAdmin)

class doctorAdmin(admin.ModelAdmin):
	list_display=["doctorID"]

admin.site.register(doctorMaster,doctorAdmin)

class SMSAdmin(admin.ModelAdmin):
	list_display=["recordID","doctor","SMSContact"]

admin.site.register(SMSlookup,SMSAdmin)




#class RawBillingRecordAdmin(admin.ModelAdmin):
