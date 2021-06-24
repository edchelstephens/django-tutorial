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
        null=True,
        related_name="managed_employees"
    )


    def __repr__(self):
        return "Employee(id={}, fullname={}, role={}, manager={})".format(
            self.id,
            self.fullname,
            self.role,
            self.manager
        )

    def __str__(self):
        return self.fullname

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)