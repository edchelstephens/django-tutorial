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
    list_per_page = 15
    list_display = ("id", "name", "date_published", "was_published_recently")
    list_filter = [ "date_published" ]
    search_fields = [ "name" ]
    date_hierarchy = "date_published"

admin.site.register(Question, QuestionAdmin)