import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models.question import Question

class QuestionModelTests(TestCase):
    """Test case for Question Model."""

    def test_str(self):
        """test Question str method."""
        name = "test"
        question = Question(name="test")
        
        self.assertEqual(str(question), name)
        self.assertEqual(question.__str__(), name)

    def test_repr(self):
        """test Question repr method."""
        name = "test"
        question = Question.objects.create(name=name, date_published=timezone.now())

        self.assertEqual(repr(question), "Question(id={}, name={})".format(question.id, name))
        self.assertEqual(question.__repr__(), "Question(id={}, name={})".format(question.id, name))

    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns False for future questions."""
        future_date = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(date_published=future_date)
        
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """was_published_recently() returns False for questions older than 1 day."""
        old_date = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(date_published=old_date)

        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        """was_published_recently() returns True for recent questions"""
        recent_date = timezone.now() - datetime.timedelta(
            hours=23, 
            minutes=59,
            seconds=59
        )
        recent_question = Question(date_published=recent_date)

        self.assertIs(recent_question.was_published_recently(), True)