from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer,UserSerializer
from .models import Vehicle,User
from django.shortcuts import render
from matplotlib.style import context


# def home(request):
#     return HttpResponse("hi homie")

class VehicleAPIView(APIView):
    """
    
    """
    def get(self, request): 
        """
        
        """
        Vehicles = Vehicle.objects.all()
        serializer =  VehicleSerializer(Vehicles, many=True)
        return Response(serializer.data)
#missing
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleDetails(APIView):
    def get_object(self, id):
        try:
            return Vehicle.objects.get(id=id)
        except Vehicle.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        Vehicle = self.get_object(id)
        serializer = VehicleSerializer(Vehicle)
        return Response(serializer.data)

    def put(self,request, id):
        Vehicle = self.get_object(id)
        serializer = VehicleSerializer(Vehicle,request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        Vehicle = self.get_object(id)
        Vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class UserAPIView(APIView):
    def get(self, request): 
        Users =  User.objects.all()
        serializer =  UserSerializer( Users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        User = self.get_object(id)
        serializer = UserSerializer(User)
        return Response(serializer.data)

    def put(self,request, id):
        User = self.get_object(id)
        serializer = UserSerializer(User,request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        User = self.get_object(id)
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def Index(request):
    vehicles = Vehicle.objects.all()
    #print(vehicle)
    context={
        "vehicles":vehicles,
    }
    return render(request,"index.html",context) 