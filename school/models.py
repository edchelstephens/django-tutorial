from django.utils.translation import gettext_lazy as _
from django.db import models

class Student(models.Model):
    "Student model class"

    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", _("Freshmane")
        SOPHOMORE = "SO", _("Sophomore")
        JUNIOR = "JR", _("Junior")
        SENIOR = "SR", _("Senior")
        GRADUATE = "GR", _("Graduate")


    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN
    )


    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR
        }