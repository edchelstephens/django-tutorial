from django.contrib import admin

from polls.models.question import Question
from polls.models.choice import Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Information", {"fields": ["name"]}),
        ("Date Information", {"fields": ["date_published"]})
    ]
    inlines = [ ChoiceInLine ]

admin.site.register(Question, QuestionAdmin)