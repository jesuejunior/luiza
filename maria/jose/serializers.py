# encoding: utf-8

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
        Employee serializer from a model
    """
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')
        extra_kwargs = {
            "email": {"validators": [UniqueValidator(queryset=Employee.objects.all(),
                                                     message="E-mail already exists")]}}
