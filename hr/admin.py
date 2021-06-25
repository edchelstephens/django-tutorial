from hr.models.employee import Employee
from hr.models.person import Person
from django.contrib import admin

from hr.models.person import Person
from hr.models.employee import Employee

class PersonAdmin(admin.ModelAdmin):
    list_display = ("fullname", "pk", "first_name", "last_name", "gender")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("pk", "person", "gender", "role", "manager")

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Person, PersonAdmin)