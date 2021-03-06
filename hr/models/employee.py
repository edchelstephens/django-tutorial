from django.db import models
from hr.models.person import Person

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
    
    # One-to-One relationship
    # One(Employee) is only One(Person)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

    # recursive many-to-one relationship to self
    # Many(employees--this Model) to One manager(the foreign key model -- Also an Employee)

    # An employee may or may not have a manager(the case for the PRESIDENT)
    # Every employee except from the President does have a manager
    # A manager can have many employees managed
    manager = models.ForeignKey(
        "self", on_delete=models.SET_NULL,
        null=True,
        related_name="managed_employees"
    )


    def __repr__(self) -> str:
        return "Employee(pk={}, person={}, role={}, manager={})".format(
            self.pk,
            repr(self.person),
            self.role,
            self.manager
        )

    def __str__(self) -> str:
        return self.fullname

    @property
    def fullname(self) -> str:
        return self.person.fullname

    @property
    def gender(self) -> str:
        return self.person.gender