from hr.models.employee import Employee
from hr.models.person import Person
from django.contrib import admin

from hr.models.person import Person
from hr.models.employee import Employee

admin.site.register(Person)
admin.site.register(Employee)