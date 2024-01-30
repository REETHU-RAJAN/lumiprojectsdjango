from django.urls import path
from exset1 import views

urlpatterns = [
    path("category/",views.CategoryCreateView.as_view(),name='category_add'),
    path("category/<int:pk>/",views.CategoryDetailView.as_view(),name='category-detail'),
    path("product/add",views.ProductCreateView.as_view(),name='product-add'),
    path("product/all",views.ProductListView.as_view(),name='product-list'),
    path("product/<int:pk>/change",views.ProductUpdateView.as_view(),name='product-update'),
     path("product/<int:pk>/remove",views.remove_product,name='product-remove'),
    path("product/<int:pk>/",views.ProductDetailView.as_view(),name='product-detail'),
]