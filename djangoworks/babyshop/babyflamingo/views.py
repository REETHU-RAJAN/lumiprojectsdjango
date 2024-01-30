from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

from babyflamingo.models import User,Category,Toys,Dress,Stationary,DressVarients,ToyVarients,StationaryVarients,Offersstationary,Offersdress,\
Offerstoy
from babyflamingo.forms import RegistrationForm,LoginForm,CategoryCreateForm,ToyAddForm,DressAddForm,StationaryAddForm,\
ToyVarientForm,Offerstoy,OfferdressForm,OffertoyForm,OfferstationaryForm,DressVarientForm,Offersdress,StationaryVarientForm,Offersstationary


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session!!")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def is_admin(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            messages.error(request,"permission denied for current user!!")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[signin_required,is_admin]
class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
        
class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("index")
            else:
                messages.error(request,"invalid creadential")
                return render(request,self.template_name,{"form":form})

@method_decorator(decs,name="dispatch")
class CatagoryCreateView(CreateView,ListView):
      template_name="category_add.html"
      form_class=CategoryCreateForm
      model=Category
      context_object_name="categories"
      success_url=reverse_lazy("add-category")

      def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form)
      def get_queryset(self):
          return Category.objects.filter(is_active=True)
      
@signin_required
@is_admin       
def remove_category(request,*args,**kwargs):
    id=kwargs.get("pk")
    Category.objects.filter(id=id).update(is_active=False)
    messages.success(request,"category removed")
    return redirect("add-category")


@signin_required

def sign_out_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin") 
    
class IndexView(TemplateView):
    template_name="index.html"


@method_decorator(decs,name="dispatch")
class ToyCreateView(CreateView):
      template_name="toy_add.html"
      form_class=ToyAddForm
      model=Toys
      
      success_url=reverse_lazy("toy-list")

      def form_valid(self, form):
        messages.success(self.request,"toy hasbeen added")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"toys adding failed")
        return super().form_invalid(form)

@method_decorator(decs,name="dispatch")
class ToyListView(ListView):
    template_name="toy_list.html"
    model=Toys
    context_object_name="toys"

@method_decorator(decs,name="dispatch")      
class ToyUpdateView(UpdateView):
      template_name="toy_edit.html"
      form_class=ToyAddForm
      model=Toys
      success_url=reverse_lazy("toy-list")
      def form_valid(self, form):
        messages.success(self.request,"toy updated sucessfully")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"toy updating failed")
        return super().form_invalid(form)

@signin_required
@is_admin 
def remove_toyview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Toys.objects.filter(id=id).delete()
    return redirect("toy-list")

@method_decorator(decs,name="dispatch")
class ToyDetailView(DetailView):
    template_name="toy_detail.html"
    model=Toys
    context_object_name="toy"

@method_decorator(decs,name="dispatch")
class DressCreateView(CreateView):
      template_name="dress_add.html"
      form_class=DressAddForm
      model=Dress
      
      success_url=reverse_lazy("dress-list")

      def form_valid(self, form):
        messages.success(self.request,"dress hasbeen added")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"dress adding failed")
        return super().form_invalid(form)

@method_decorator(decs,name="dispatch")
class DressListView(ListView):
    template_name="dress_list.html"
    model=Dress
    context_object_name="dress"

@method_decorator(decs,name="dispatch")      
class DressUpdateView(UpdateView):
      template_name="dress_edit.html"
      form_class=DressAddForm
      model=Dress
      success_url=reverse_lazy("dress-list")
      def form_valid(self, form):
        messages.success(self.request,"dress updated sucessfully")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"dress updating failed")
        return super().form_invalid(form)

@signin_required
@is_admin 
def remove_dressview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Dress.objects.filter(id=id).delete()
    return redirect("dress-list")

@method_decorator(decs,name="dispatch")
class DressDetailView(DetailView):
    template_name="dress_detail.html"
    model=Dress
    context_object_name="dress"
@method_decorator(decs,name="dispatch")
class StationaryCreateView(CreateView):
      template_name="stationary_add.html"
      form_class=StationaryAddForm
      model=Stationary
      
      success_url=reverse_lazy("stationary-list")

      def form_valid(self, form):
        messages.success(self.request,"stationary hasbeen added")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"stationary adding failed")
        return super().form_invalid(form)

@method_decorator(decs,name="dispatch")
class StationaryListView(ListView):
    template_name="stationary_list.html"
    model=Stationary
    context_object_name="stationary"

@method_decorator(decs,name="dispatch")      
class StationaryUpdateView(UpdateView):
      template_name="stationary_edit.html"
      form_class=StationaryAddForm
      model=Stationary
      success_url=reverse_lazy("stationary-list")
      def form_valid(self, form):
        messages.success(self.request,"stationary updated sucessfully")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"stationary updating failed")
        return super().form_invalid(form)

@signin_required
@is_admin 
def remove_stationaryview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Stationary.objects.filter(id=id).delete()
    return redirect("stationary-list")

@method_decorator(decs,name="dispatch")
class StationaryDetailView(DetailView):
    template_name="stationary_detail.html"
    model=Stationary
    context_object_name="stationary"

@method_decorator(decs,name="dispatch")
class ToyVarientCreateView(CreateView):
    template_name="toyvarient_add.html"
    form_class=ToyVarientForm
    model=ToyVarients
    success_url=reverse_lazy("toy-list")

    def form_valid(self, form ):
        id=self.kwargs.get("pk")
        obj=Toys.objects.get(id=id)
        form.instance.toy=obj
        messages.success(self.request,"varient has been added")
        return super().form_valid(form)    

@method_decorator(decs,name="dispatch")
class ToyVarientUpdateView(UpdateView):
    template_name="toyvarient_edit.html"
    form_class=ToyVarientForm
    model=ToyVarients
    success_url=reverse_lazy("toy-list")
    def form_valid(self, form):
        messages.success(self.request,"toy varient updated sucessfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"toy varient updating failed")
        return super().form_invalid(form)
    def get_success_url(self):
        id=self.kwargs.get("pk")
        toy_varient_object=ToyVarients.objects.get(id=id)
        toy_id=toy_varient_object.toy.id
        return reverse("toy-detail",kwargs={"pk":toy_id})

@signin_required
@is_admin 
def remove_toyvarientview(request,*args,**kwargs):
   
    id=kwargs.get("pk")
    ToyVarients.objects.filter(id=id).delete()
    return redirect("toy-list")    

@method_decorator(decs,name="dispatch")
class OffertoyCreateView(CreateView):
    template_name="offertoy_add.html"

    form_class=OffertoyForm
    model=Offerstoy
    success_url=reverse_lazy("toy-list")
    def form_valid(self, form ):
        id=self.kwargs.get("pk")
        obj=ToyVarients.objects.get(id=id)
        form.instance.ToyVarient=obj
        messages.success(self.request,"offer has been added")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed")
        return super().form_invalid(form)
    def get_success_url(self):
        id=self.kwargs.get("pk")
        toy_varient_object=ToyVarients.objects.get(id=id)
        toy_id=toy_varient_object.toy.id
        return reverse("toy-detail",kwargs={"pk":toy_id})

@signin_required
@is_admin 
def offertoy_delete_view(request,*args,**kwargs):
   
    id=kwargs.get("pk")
    offer_object=Offerstoy.objects.get(id=id)
    toy_id=offer_object.toyvarient.toy.id
    offer_object.delete()
    return redirect("toy-detail",pk=toy_id)


@method_decorator(decs,name="dispatch")
class StationaryVarientCreateView(CreateView):
    template_name="stationaryvarient_add.html"
    form_class=StationaryVarientForm
    model=StationaryVarients
    success_url=reverse_lazy("stationary-list")

    def form_valid(self, form ):
        id=self.kwargs.get("pk")
        obj=Stationary.objects.get(id=id)
        form.instance.Stationary=obj
        messages.success(self.request,"varient has been added")
        return super().form_valid(form)    

@method_decorator(decs,name="dispatch")
class StationaryVarientUpdateView(UpdateView):
    template_name="stationaryvarient_edit.html"
    form_class=StationaryVarientForm
    model=StationaryVarients
    success_url=reverse_lazy("stationary-list")
    def form_valid(self, form):
        messages.success(self.request,"stationary varient updated sucessfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"stationary varient updating failed")
        return super().form_invalid(form)
    def get_success_url(self):
        id=self.kwargs.get("pk")
        stationary_varient_object=StationaryVarients.objects.get(id=id)
        stationary_id=stationary_varient_object.stationary.id
        return reverse("stationary-detail",kwargs={"pk":stationary_id})

@signin_required
@is_admin 
def remove_stationaryvarientview(request,*args,**kwargs):
   
    id=kwargs.get("pk")
    StationaryVarients.objects.filter(id=id).delete()
    return redirect("stationary-list")    

@method_decorator(decs,name="dispatch")
class OfferstationaryCreateView(CreateView):
    template_name="offerstationary_add.html"

    form_class=OfferstationaryForm
    model=Offersstationary
    success_url=reverse_lazy("stationary-list")
    def form_valid(self, form ):
        id=self.kwargs.get("pk")
        obj=StationaryVarients.objects.get(id=id)
        form.instance.stationaryvarient=obj
        messages.success(self.request,"offer has been added")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed")
        return super().form_invalid(form)
    def get_success_url(self):
        id=self.kwargs.get("pk")
        stationary_varient_object=StationaryVarients.objects.get(id=id)
        stationary_id=stationary_varient_object.stationary.id
        return reverse("stationary-detail",kwargs={"pk":stationary_id})

@signin_required
@is_admin 
def offerstationary_delete_view(request,*args,**kwargs):
   
    id=kwargs.get("pk")
    offer_object=Offersstationary.objects.get(id=id)
    stationary_id=offer_object.stationaryvarient.stationary.id
    offer_object.delete()
    return redirect("stationary-detail",pk=stationary_id)



@method_decorator(decs,name="dispatch")
class DressVarientCreateView(CreateView):
    template_name="dressvarient_add.html"
    form_class=DressVarientForm
    model=DressVarients
    success_url=reverse_lazy("dress-list")

    def form_valid(self, form ):
        id=self.kwargs.get("pk")
        obj=Dress.objects.get(id=id)
        form.instance.dress=obj
        messages.success(self.request,"varient has been added")
        return super().form_valid(form)    

@method_decorator(decs,name="dispatch")
class DressVarientUpdateView(UpdateView):
    template_name="dressvarient_edit.html"
    form_class=DressVarientForm
    model=DressVarients
    success_url=reverse_lazy("dress-list")
    def form_valid(self, form):
        messages.success(self.request,"dress varient updated sucessfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"dress varient updating failed")
        return super().form_invalid(form)
    def get_success_url(self):
        id=self.kwargs.get("pk")
        dress_varient_object=DressVarients.objects.get(id=id)
        dress_id=dress_varient_object.dress.id
        return reverse("dress-detail",kwargs={"pk":dress_id})

@signin_required
@is_admin 
def remove_dressvarientview(request,*args,**kwargs):
   
    id=kwargs.get("pk")
    DressVarients.objects.filter(id=id).delete()
    return redirect("dress-list")    

@method_decorator(decs,name="dispatch")
class OfferdressCreateView(CreateView):
    template_name="offerdress_add.html"

    form_class=OfferdressForm
    model=Offersdress
    success_url=reverse_lazy("dress-list")
    def form_valid(self, form ):
        id=self.kwargs.get("pk")
        obj=DressVarients.objects.get(id=id)
        form.instance.DressVarient=obj
        messages.success(self.request,"offer has been added")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"failed")
        return super().form_invalid(form)
    def get_success_url(self):
        id=self.kwargs.get("pk")
        dress_varient_object=DressVarients.objects.get(id=id)
        dress_id=dress_varient_object.dress.id
        return reverse("dress-detail",kwargs={"pk":dress_id})

@signin_required
@is_admin 
def offerdress_delete_view(request,*args,**kwargs):
   
    id=kwargs.get("pk")
    offer_object=Offersdress.objects.get(id=id)
    dress_id=offer_object.dressvarient.dress.id
    offer_object.delete()
    return redirect("dress-detail",pk=dress_id)