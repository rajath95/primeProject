from django.contrib import admin
from .models import Profile,Commodities,doctorMaster,serviceCodeMaster,SMSlookup,HospitalRevenue
from .models import specializatonMaster
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
	list_display = ["doctorID"]

admin.site.register(doctorMaster,doctorAdmin)

class SMSAdmin(admin.ModelAdmin):
	list_display=["recordID","doctor","SMSContact"]

admin.site.register(SMSlookup,SMSAdmin)


class HospitalRevenueAdmin(admin.ModelAdmin):

	list_display=["recordID","month","week","avg_pharma","avg_lab","avg_rad","act_lab","act_pharma","act_rad"]
	WEEK_NO= (('1','1'),('2','2'),('3','3'),('4','4'),)

admin.site.register(HospitalRevenue,HospitalRevenueAdmin)

class specializatonMasterAdmin(admin.ModelAdmin):
	list_display=specializatonMaster._meta.get_all_field_names()

admin.site.register(specializatonMaster,specializatonMasterAdmin)

class serviceCodeMasterAdmin(admin.ModelAdmin):
	list_display=serviceCodeMaster._meta.get_all_field_names()

admin.site.register(serviceCodeMaster,serviceCodeMasterAdmin)


#admin.site.register(doctorMaster,doctorMasterAdmin)

#class RawBillingRecordAdmin(admin.ModelAdmin):
