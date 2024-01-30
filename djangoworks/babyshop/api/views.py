from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from babyflamingo.models import User,Toys,ToyVarients,Cartsdress,Cartsstationary,Cartstoy,StationaryVarients,DressVarients,Dress,Stationary,Orderstoy,Ordersdress,Ordersstationary,Reviewstoy,Reviewsdress,Reviewsstationary,Offerstoy,Offersdress,Offersstationary
from api.serializers import UserSerializer,OffertoySerializer,OrdertoySerializer,ReviewtoySerializer,ToysSerializer,ToyVarientSerializer,CartTOYSerializer



class ToyViewsetView(viewsets.ModelViewSet):
    serializer_class=ToysSerializer
    model=Toys
    queryset=Toys.objects.all()
