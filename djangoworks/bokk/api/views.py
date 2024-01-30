from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response

from api.models import bokks
from api.serializers import BooksSerializer



class BOOKViewsetView(viewsets.ModelViewSet):
    serializer_class=BooksSerializer
    model=bokks
    queryset=bokks.objects.all()