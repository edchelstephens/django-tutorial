from django.conf import settings
from django.db import models

class Person(models.Model):
    """Human person model."""

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=Gender.choices, blank=True)
    friends = models.ManyToManyField("self")


    def __repr__(self) -> str:
        return "Person(pk={}, fullname={})".format(
            self.pk,
            self.fullname
        )

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def fullname(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)


class Trainee(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    supervisor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="supervised_trainee"
    )

    def __repr__(self) -> str:
        return "Trainee(user={}, supervisor={})".format(
            self.user,
            self.supervisor
        )