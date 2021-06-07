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
        """Questions with date_published in the past are displayed on index page."""
        question = create_question(name="Past question.", days=-30)
        response = self.client.get(self.url)

        self.assertQuerysetEqual(
            response.context["latest_polls"],
            ["Question(id={}, name=Past question.)".format(question.id)]
        )

    def test_future_question(self):
        """Questions with date_published in the future are not displayed on the index page."""
        question = create_question(name="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))

        self.assertContains(response, "No polls are available")

    def test_future_and_past_question(self):
        """Even if both past and future question are present, only past questions are showed."""
        past_question = create_question(name="Past question.", days=-30)
        future_question = create_question(name="Past question.", days=30)
        response = self.client.get(reverse("polls:index"))
        
        self.assertQuerysetEqual(response.context["latest_polls"],[
            "Question(id={}, name={})".format(past_question.id, past_question.name)
        ])

    def test_two_past_questions(self):
        """Index page will display multiple past questions(the latest 5)."""
        q1 = create_question(name="Q1", days=-1)
        q2 = create_question(name="Q2", days=-2)
        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(response.context["latest_polls"],[
            "Question(id={}, name={})".format(q1.id, q1.name),
            "Question(id={}, name={})".format(q2.id, q2.name)           
        ])

    def test_past_six_questions(self):
        """Index page will display only the latest 5 questions."""
        q1 = create_question(name="Q1", days=-1)
        q2 = create_question(name="Q2", days=-2)
        q3 = create_question(name="Q3", days=-3)
        q4 = create_question(name="Q4", days=-4)
        q5 = create_question(name="Q5", days=-5)
        q6 = create_question(name="Q6", days=-6)
        q7 = create_question(name="Q7", days=-7)
        q8 = create_question(name="Q8", days=-8)

        response = self.client.get(reverse("polls:index"))

        self.assertQuerysetEqual(response.context["latest_polls"],[
            "Question(id={}, name={})".format(q1.id, q1.name),
            "Question(id={}, name={})".format(q2.id, q2.name),
            "Question(id={}, name={})".format(q3.id, q3.name),
            "Question(id={}, name={})".format(q4.id, q4.name),
            "Question(id={}, name={})".format(q5.id, q5.name),
        ])