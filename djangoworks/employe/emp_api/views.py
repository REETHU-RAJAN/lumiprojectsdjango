from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from emp.models import employee
from emp_api.serializers import EmployeeSerializer

# Create your views here.

class EmployeeViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=employee.objects.get(id=id)

        serializer=EmployeeSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=employee.objects.get(id=id)
        serializer=EmployeeSerializer(qs)
        return Response(data=serializer.data)
       
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        employee.objects.filter(id=id).delete()
        return Response(data={"message":"employee deleted"})
