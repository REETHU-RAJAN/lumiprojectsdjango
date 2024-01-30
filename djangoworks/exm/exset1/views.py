from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from exset1.forms import CategoryForm,ProductChangeForm,ProductForm
from exset1.models import Category,Product
from django.views.generic import View,CreateView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy

class CategoryCreateView(CreateView,ListView):
    template_name="category_add.html"
    form_class= CategoryForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("category_add")

class CategoryDetailView(DetailView):
    template_name="category_detail.html"
    context_object_name="categories"
    model=Category
   

    


class ProductCreateView(CreateView):
   

    template_name="product_add.html"
    form_class=ProductForm
    model=Product
    success_url=reverse_lazy("product-add")
   

class ProductListView(ListView):
   
    template_name="prod_list.html"
    model=Product
    context_object_name="prod"



class ProductUpdateView(UpdateView):
   
    template_name="prod_update.html"
    success_url=reverse_lazy("product-list")
    form_class=ProductChangeForm
    model=Product

class ProductDetailView(DetailView):
    template_name="productdetail.html"
    model=Product
    context_object_name="p"
    

def remove_product(request,args,*kwargs):
    id=kwargs.get("pk")
    Product.objects.get(id=id).delete()
    return redirect("product-list")
  