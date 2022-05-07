from operator import index
from django.urls import URLPattern, path
from .views import VehicleAPIView,VehicleDetails,UserAPIView,UserDetails
from . import views

app_name = 'vehiclemanagement'

urlpatterns = [
    # path('', MyView.as_view(), name='index'),
    path('', VehicleAPIView.as_view()),
    path('vmanage/<int:id>', VehicleDetails.as_view()),
    path('', UserAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path("index",views.Index, name="index" )

]