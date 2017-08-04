# encoding: utf-8
from __future__ import unicode_literals

import json

import pytest
from model_mommy import mommy

from .models import Employee


@pytest.mark.django_db
class EmployeeModelTest:

    def test_create_correct_user(self):
        data = {
            "name": "João da Silva",
            "email": "joao@silva.org",
            "department": "mobile",
        }

        user = Employee.objects.create(**data)
        assert user.id == 1
        assert user.name == 'João da Silva'
        assert user.email == 'joao@silva.org'
        assert user.department == 'mobile'


@pytest.mark.django_db
class EmployeeApiTest:
    @pytest.fixture(autouse=True)
    def setUp(self, client):
        self.client = client

    def test_create_employee_ok(self):
        data = {
            "name": "João da Silva",
            "email": "joao@silva.org",
            "department": "mobile",
        }
        response = self.client.post('/employee/', data=json.dumps(data),
                                    content_type='application/json')
        assert response.status_code == 201

    def test_create_employee_with_wrong_data(self):
        data = {
            "name": "João da Silva",
            "department": "mobile",
        }
        response = self.client.post('/employee/', data=json.dumps(data),
                                    content_type='application/json')
        assert response.status_code == 400

    def test_email_exist_return_error(self):
        mommy.make_one(Employee, email='joao@silva.org')
        data = {
            "name": "João de Melo",
            "email": "joao@silva.org",
            "department": "mobile",
        }

        response = self.client.post('/employee/', data=json.dumps(data),
                                    content_type='application/json')
        assert response.status_code == 400
        assert response.data.get('message') == u'E-mail already exists'

    def test_create_employee_and_saved_into_db(self):
        data = {
            "name": "João da Silva",
            "email": "joao@silva.org",
            "department": "mobile",
        }
        self.client.post('/employee/', data=json.dumps(data),
                         content_type='application/json')
        employee = Employee.objects.get(email='joao@silva.org')

        assert employee.name == u'João da Silva'
        assert employee.email == 'joao@silva.org'
        assert employee.department == 'mobile'

    def test_list_empty_employees(self):
        response = self.client.get('/employee/', content_type='application/json')
        assert response.data == []

    def test_list_with_some_employees(self):
        mommy.make_many(Employee, 5)
        response = self.client.get('/employee/', content_type='application/json')
        assert len(response.data) == 5

    def test_delete_employee(self):
        mommy.make_one(Employee, id=1)
        mommy.make_many(Employee, 5)
        response = self.client.delete('/employee/1', content_type='application/json')
        assert response.status_code == 204

    def test_try_delete_employee_not_found(self):
        mommy.make_many(Employee, 5)
        response = self.client.delete('/employee/1', content_type='application/json')
        assert response.status_code == 204

    def test_delete_employee_check_in_db(self):
        mommy.make_one(Employee, id=1)
        mommy.make_many(Employee, 5)

        assert Employee.objects.count() == 6

        self.client.delete('/employee/1', content_type='application/json')

        assert Employee.objects.count() == 5
