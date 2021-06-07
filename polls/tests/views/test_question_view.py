import datetime

from django.http import response
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from polls.models.question import Question



def create_question(name, days):
    """Create a question with the given name and published after given days."""
    date_published = timezone.now() + datetime.timedelta(days=days)

    return Question.objects.create(name=name, date_published=date_published)

class QuestionIndexViewTests(TestCase):
    """Test case for question index view."""
    url = reverse("polls:index")
    
    def test_no_questions(self):
        """If no questions exists, set 'no polls message' should be displayed."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_polls"], [])

    def test_past_question(self):
        """Question with date_published in the past are displayed on index page."""
        question = create_question(name="Past question.", days=-30)
        response = self.client.get(self.url)
        self.assertQuerysetEqual(
            response.context["latest_polls"],
            ["Question(id={}, name=Past question.)".format(question.id)]
        )