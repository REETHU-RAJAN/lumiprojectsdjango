from django.urls import path
from testb.views import CatagoryCreateView,ProductCreateView,\
ProductListView,ProductUpdateView,remove_productview
urlpatterns = [
    
    
    path("categories/add",CatagoryCreateView.as_view(),name="add-category"),

    path("products/add",ProductCreateView.as_view(),name="product-add"),
    path("products/all",ProductListView.as_view(),name="product-list"),
    path("products/<int:pk>/change",ProductUpdateView.as_view(),name="product-change"),
    path("products/<int:pk>/remove",remove_productview,name="product-remove"),
]    