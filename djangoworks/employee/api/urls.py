from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("employees",views.EmployeeView,basename="employees")




urlpatterns = [
    
  

]+router.urls