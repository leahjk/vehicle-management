from django.db import models
from django.utils.translation import gettext_lazy as _
from .modelUser import User
   
class Vehicle(models.Model):
    type = models.CharField(max_length=30, blank=False)
    numberPlate = models.CharField(max_length=7, unique=True)
    yearofmanufacture = models.DateField()  
    capacity = models.PositiveIntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name= 'cars')
    updatedAt = models.DateTimeField(auto_now=True)

    #order so that the latest entries appear first according to the yearmanufacture
    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")
        ordering = ['-yearofmanufacture']

    def __str__(self):
        return self.type
