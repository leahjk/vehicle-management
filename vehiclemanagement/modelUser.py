from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    firstName = models.CharField(max_length= 255)
    lastName = models.CharField(max_length= 255)
    username = models.CharField(max_length= 255)
    phoneNumber = models.IntegerField()
    dateOfBirth = models.DateField()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username