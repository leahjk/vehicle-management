from argparse import Namespace
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
        #in order to be able to easily reference the urls on  the web page
    path('vehicle/',include('vehiclemanagement.urls')),

    ]
