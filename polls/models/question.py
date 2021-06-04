import datetime

from django.db import models
from django.utils import timezone

from polls.models.abstract import NamedModel

class Question(NamedModel):
    """The poll question model."""
    date_published = models.DateTimeField("date published")

    def __repr__(self):
        return "Question(id={}, name={})".format(
            self.id,
            self.name
        )

    def was_published_recently(self):
        """Check if question was published recently"""
        now = timezone.now()
        recent = now - datetime.timedelta(days=1)
        return recent <= self.date_published <= now
