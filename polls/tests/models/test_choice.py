from django.test import TestCase
from django.utils import timezone

from polls.models.question import Question
from polls.models.choice import Choice

class ChoiceModelTestCase(TestCase):
    """Test case for choice model."""

    def test_str(self):
        """test choice str method."""
        name = "choice"
        choice = Choice(name=name)

        self.assertEqual(str(choice), name)
        self.assertEqual(choice.__str__(), name)

    def test__repr(self):
        """test choice repr method"""
        question_name = "test_question"
        question = Question.objects.create(name=question_name, date_published=timezone.now())
        choice_name = "test_choice"
        choice = Choice.objects.create(name=choice_name, question=question)

        self.assertEqual(repr(choice), "Choice(name={}, question=Question(id={}, name={}), votes={}".format(
            choice_name,
            question.id,
            question_name,
            choice.votes
        ))
        self.assertEqual(choice.__repr__(), "Choice(name={}, question=Question(id={}, name={}), votes={}".format(
            choice_name,
            question.id,
            question_name,
            choice.votes
        ))
