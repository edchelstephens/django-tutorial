from django.contrib import admin

from polls.models.question import Question
from polls.models.choice import Choice

admin.site.register(Question)
admin.site.register(Choice)
