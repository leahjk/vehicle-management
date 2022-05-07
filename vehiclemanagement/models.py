from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    firstName = models.CharField(max_length= 30,blank=False)
    lastName = models.CharField(max_length= 30,blank=False)
    username = models.CharField(max_length= 30,unique=True)
    phone_number = models.PositiveIntegerField(default="+254712345678")
    dob = models.DateField(blank=False)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ['-phone_number']

    def __str__(self):
        return self.username

   
class Vehicle(models.Model):
    type = models.CharField(max_length=30, blank=False)
    number_plate = models.CharField(max_length=7, unique=True)
    yom = models.DateField()  
    capacity = models.PositiveIntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name= 'cars')
    updated_at = models.DateTimeField(auto_now=True)

    #order so that the latest entries appear first according to the yearmanufacture
    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")
        ordering = ['-yom']

    def __str__(self):
        return self.type
