import datetime

from django.db import models
from django.utils import timezone

from polls.models.question import Question
from polls.models.abstract import NamedModel


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
