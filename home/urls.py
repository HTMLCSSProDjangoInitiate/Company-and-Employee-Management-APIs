
from django.urls import include, path
from rest_framework import routers

from home.views import CompanyViewSet, EmployeeViewSet

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]