from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer,UserSerializer
from .models import Vehicle,User
from django.shortcuts import get_object_or_404, render
from matplotlib.style import context

class VehicleAPIView(APIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    def get(self, request): 
        serializer =  self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class VehicleDetails(APIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    def get_object(self, id):
        return get_object_or_404(self.queryset,id=id)
       
    def get(self, request, id):
        Vehicle = self.get_object(id)
        serializer = self.serializer_class(Vehicle)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request, id):
        Vehicle = self.get_object(id)
        serializer = VehicleSerializer(Vehicle,request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        Vehicle = self.get_object(id)
        Vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class UserAPIView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request): 
        serializer =  self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

     


class UserDetails(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_object(self, id):
        return get_object_or_404(self.queryset,id=id)

    def get(self, request, id):
        User = self.get_object(id)
        serializer = self.serializer_class(User)
        return Response(serializer.data)

    def put(self,request, id):
        User = self.get_object(id)
        serializer = self.serializer_class(User,request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_201_CREATED)

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