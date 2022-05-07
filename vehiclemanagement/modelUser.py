from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    firstName = models.CharField(max_length= 30,blank=False)
    lastName = models.CharField(max_length= 30,blank=False)
    username = models.CharField(max_length= 30,unique=True)
    phoneNumber = models.PositiveIntegerField(default="+254712345678")
    dateOfBirth = models.DateField(blank=False)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
