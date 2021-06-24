from django.db import models

class Person(models.Model):
    """Human person model."""

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=Gender.choices, blank=True)


    def __repr__(self) -> str:
        return "Person(id={}, fullname={})".format(
            self.id,
            self.first_name,
            self.last_name
        )

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def fullname(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)