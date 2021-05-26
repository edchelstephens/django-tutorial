from django.db import models

class NamedModel(models.Model):
    """Abstract base class for models with name fields."""
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name