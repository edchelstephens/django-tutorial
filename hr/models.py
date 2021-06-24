from django.db import models
from django.db.models import manager

class Employee(models.Model):
    """Employee model."""

 
    class EMPLOYEE_ROLES(models.TextChoices):
        STANDARD = "STANDARD", "Basic employee",
        HR = "HR", "Human resources"
        SUPERVISOR = "SUPERVISOR", "Supervisor",
        MANAGER = "MANAGER", "Manager",
        PRESIDENT = "PRESIDENT", "President"

    role = models.CharField(
        max_length=50, 
        choices=EMPLOYEE_ROLES.choices, 
        default=EMPLOYEE_ROLES.STANDARD
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    manager = models.ForeignKey(
        "self", on_delete=models.SET_NULL,
        null=True
    )
