from django.contrib import admin
from .models import Profile,Commodities,RawBillingRecord,BadBillingRecord
from .forms import SignupForm
# Register your models here.

class  ProfileAdmin(admin.ModelAdmin):

	list_display=["username","first_name","last_name","email","role","mobile","date"]
	form=SignupForm



admin.site.register(Profile,ProfileAdmin)

class CommodityAdmin(admin.ModelAdmin):
	list_display=["commodity","price"]


admin.site.register(Commodities,CommodityAdmin)

class RawBillingRecordAdmin(admin.ModelAdmin):
	list_display = RawBillingRecord._meta.get_all_field_names()

admin.site.register(RawBillingRecord,RawBillingRecordAdmin)

class BadBillingRecordAdmin(admin.ModelAdmin):
	list_display = BadBillingRecord._meta.get_all_field_names()
	
admin.site.register(BadBillingRecord,BadBillingRecordAdmin)





#class RawBillingRecordAdmin(admin.ModelAdmin):