from django.db import models

from polls.models.abstract import NamedModel

class Question(NamedModel):
    """The poll question model."""
    date_published = models.DateTimeField("date published")

    def __repr__(self):
        return f"Question(name={self.name})"

class Choice(NamedModel):
    """Poll question answer choices model with votes."""
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, 
        related_name="choices"
    )
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return f"Choice(name={self.name}, question={repr(self.question)}, votes={self.votes}"
    
    def __str__(self):
        return self.name