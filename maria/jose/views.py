# encoding: utf-8
import logging
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import EmployeeSerializer

logger = logging.getLogger(__name__)


class EmployeeView(APIView):
    """
        List all employee, or create a new employee.
    """
    def get(self, request, format=None):
        """
        :param request:
        :param format:
        :return: All Employee
        """
        logger.info('action: getting_employees')
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Creating a new Employee
        :param request:
        :param format:
        :return:
        """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        # FIXME: Improve this error log
        try:
            response = {'message': serializer.errors.get('email')[0]}
        except:
            response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):
    """
        Retrieve, update or delete a employee instance.
    """

    def delete(self, request, pk, format=None):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
        finally:
            return Response(status=status.HTTP_204_NO_CONTENT)
