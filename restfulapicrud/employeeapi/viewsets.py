from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

# list(), retrieve(), create(), updtae(), destroy() provides this viewsets