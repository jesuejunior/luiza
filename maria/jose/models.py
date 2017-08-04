from django.db import models


class Employee(models.Model):
    name = models.CharField(verbose_name='Name', max_length=60)
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True)
    department = models.CharField(verbose_name='Department', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = u'employee'
        app_label = u'jose'
        verbose_name = u'Employee'
