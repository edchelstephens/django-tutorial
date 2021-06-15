from django.contrib import admin

from polls.models.question import Question
from polls.models.choice import Choice

admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    fields = ["date_published", "name"]

admin.site.register(Question, QuestionAdmin)