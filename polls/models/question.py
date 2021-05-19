from django.db import models

from polls.models.abstract import NamedModel

class Question(NamedModel):
    """The poll question."""
    pub_date = models.DateTimeField("date published")

class Choice(NamedModel):
    """Poll question answer choices with votes."""
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, 
        related_name="choices"
    )
    votes = models.IntegerField(default=0)