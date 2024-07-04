from rest_framework import viewsets
from django.shortcuts import render

from home.models import Employee, company
from home.serializers import CompanySerializer, EmployeeSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset= company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


