from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DetailView,TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View


from testb.models import Category,Products
from testb.forms import CategoryCreateForm,ProductAddForm
    


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
      



class ProductCreateView(CreateView):
      template_name="product_add.html"
      form_class=ProductAddForm
      model=Products
      
      success_url=reverse_lazy("product-add")

      def form_valid(self, form):
        messages.success(self.request,"product hasbeen added")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"products adding failed")
        return super().form_invalid(form)




class ProductListView(ListView):
    template_name="product_list.html"
    model=Products
    context_object_name="products"

     
class ProductUpdateView(UpdateView):
      template_name="product_edit.html"
      form_class=ProductAddForm
      model=Products
      success_url=reverse_lazy("product-list")
      def form_valid(self, form):
        messages.success(self.request,"product updated sucessfully")
        return super().form_valid(form)
    
      def form_invalid(self, form):
        messages.error(self.request,"product updating failed")
        return super().form_invalid(form)


def remove_productview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Products.objects.filter(id=id).delete()
    return redirect("product-list")


    
