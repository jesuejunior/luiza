# encoding: utf-8

from django.conf.urls import url

from .views import EmployeeView, EmployeeDetailView

urlpatterns = [
    url(r'^employee/(?P<pk>[0-9]+)', EmployeeDetailView.as_view()),
    url(r'^employee/', EmployeeView.as_view()),
]
