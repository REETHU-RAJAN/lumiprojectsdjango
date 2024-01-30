from rest_framework import serializers
from api.models import employee

 

class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
   

    class Meta:
        model=employee
        fields="__all__"     