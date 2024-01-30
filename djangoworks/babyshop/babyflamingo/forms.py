from django import forms
from babyflamingo.models import User,Category,Toys,Dress,Stationary,ToyVarients,DressVarients,StationaryVarients,Offersdress,Offersstationary,Offerstoy
from django.contrib.auth.forms import UserCreationForm
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","address"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]
class ToyAddForm(forms.ModelForm):
    class Meta:
        model=Toys
        fields="__all__"      

class DressAddForm(forms.ModelForm):
    class Meta:
        model=Dress
        fields="__all__"  

class StationaryAddForm(forms.ModelForm):
    class Meta:
        model=Stationary
        fields="__all__"  

class ToyVarientForm(forms.ModelForm):
    class Meta:
        model=ToyVarients
        exclude=("toy",)            
      
class OffertoyForm(forms.ModelForm):
    class Meta:
        model=Offerstoy
        exclude=("toyvarient",)
        widgets={
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "due_date":forms.DateInput(attrs={"type":"date"})



        }     

class DressVarientForm(forms.ModelForm):
    class Meta:
        model=DressVarients
        exclude=("dress",)            
      
class OfferdressForm(forms.ModelForm):
    class Meta:
        model=Offersdress
        exclude=("dressvarient",)
        widgets={
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "due_date":forms.DateInput(attrs={"type":"date"})



        }            

class StationaryVarientForm(forms.ModelForm):
    class Meta:
        model=StationaryVarients
        exclude=("stationary",)            
      
class OfferstationaryForm(forms.ModelForm):
    class Meta:
        model=Offersstationary
        exclude=("stationaryvarient",)
        widgets={
            "start_date":forms.DateInput(attrs={"type":"date"}),
            "due_date":forms.DateInput(attrs={"type":"date"})



        }            