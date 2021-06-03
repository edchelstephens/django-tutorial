import datetime

from django.db import models
from django.utils import timezone

from polls.models.abstract import NamedModel

class Question(NamedModel):
    """The poll question model."""
    date_published = models.DateTimeField("date published")

    def __str__(self):
        return self.name

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

class Choice(NamedModel):
    """Poll question answer choices model with votes."""
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, 
        related_name="choices"
    )
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return "Choice(id={}, name={}, question={}, votes={})".format(
            self.id,
            self.name,
            repr(self.question),
            self.votes
        )
