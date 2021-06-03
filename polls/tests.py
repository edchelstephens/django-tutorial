import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question

class QuestionModelTests(TestCase):
    """Test case for Question Model."""

    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns False for future questions."""

        future_date = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(date_published=future_date)
        
        self.assertIs(future_question.was_published_recently(), False)

    def test_repr(self):
        """test Question repr method."""
        name = "test"
        question = Question.objects.create(name=name, date_published=timezone.now())
        self.assertEqual(repr(question), "Question(id={}, name={})".format(question.id, name))
