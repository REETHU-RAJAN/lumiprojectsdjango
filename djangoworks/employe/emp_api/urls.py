from django.urls import path
from emp_api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("employees",views.EmployeeViewSetView,basename="employees")

urlpatterns=[

]+router.urls