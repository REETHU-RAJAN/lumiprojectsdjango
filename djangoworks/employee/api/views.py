from django.shortcuts import render
from api.models import employee
from api.serializer import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import authentication
from rest_framework import permissions
# Create your views here.
class EmployeeView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=employee.objects.all()