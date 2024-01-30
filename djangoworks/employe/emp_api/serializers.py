from emp.models import employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model=employee
        fields="__all__"