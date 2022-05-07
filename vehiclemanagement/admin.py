from django.contrib import admin
from vehiclemanagement.models import Vehicle
from vehiclemanagement.modelUser import User
# Register your models here.

#Customizing how the entries are displayed on the admin portal

class VehicleAdminModel(admin.ModelAdmin):
    list_display = ("type","numberPlate","owner", "updatedAt")
    search_fields = ("type","numberPlate","owner__username","updatedAt")


class UserAdminModel(admin.ModelAdmin):
    list_display = ("firstName", "dateOfBirth")



admin.site.register(Vehicle,VehicleAdminModel)
admin.site.register(User,UserAdminModel)
