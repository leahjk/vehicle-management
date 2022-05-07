from django.contrib import admin
from vehiclemanagement.models import Vehicle, User
# Register your models here.

#Customizing how the entries are displayed on the admin portal

class VehicleAdminModel(admin.ModelAdmin):
    list_display = ("type","number_plate","owner", "updated_at")
    search_fields = ("type","number_plate","owner__username","updated_at")


class UserAdminModel(admin.ModelAdmin):
    list_display = ("firstName", "dob")



admin.site.register(Vehicle,VehicleAdminModel)
admin.site.register(User,UserAdminModel)
