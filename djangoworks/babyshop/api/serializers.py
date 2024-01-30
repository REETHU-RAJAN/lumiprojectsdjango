from rest_framework import serializers
from babyflamingo.models import User,Toys,ToyVarients,Cartsdress,Cartsstationary,Cartstoy,StationaryVarients,DressVarients,Dress,Stationary,Orderstoy,Ordersdress,Ordersstationary,Reviewstoy,Reviewsdress,Reviewsstationary,Offerstoy,Offersdress,Offersstationary

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)  

class OffertoySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    price=serializers.CharField(read_only=True)
    start_date=serializers.CharField(read_only=True) 
    due_date=serializers.CharField(read_only=True) 

    class Meta:
        model=Offerstoy
        exclude=("toyvarient",)       

class ToyVarientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    offerstoy=OffertoySerializer(read_only=True,many=True)
    class Meta:
        model=ToyVarients      
        exclude=("toy",)  

class ReviewtoySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    toy=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)       
    class Meta:
        model=Reviewstoy
        fields="__all__"
class ToysSerializer(serializers.ModelSerializer):
    # category=serializers.StringRelatedField(read_only=True)
    category=serializers.SlugRelatedField(read_only=True,slug_field="name")
    varients=ToyVarientSerializer(many=True,read_only=True)
    reviews=ReviewtoySerializer(many=True,read_only=True)
    avg_rating=serializers.CharField(read_only=True)
    class Meta:
        model=Toys
        fields="__all__"


class CartTOYSerializer(serializers.ModelSerializer):
    toyvarient=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Cartstoy
        fields=["toyvarient","user","status","date"]

class OrdertoySerializer(serializers.ModelSerializer):
    toyvarient=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    orderd_date=serializers.CharField(read_only=True)
    expected_date=serializers.CharField(read_only=True)
    
    class Meta:
        model=Orderstoy
        fields=["toyvarient","user","status","orderd_date","expected_date","address"]        

        