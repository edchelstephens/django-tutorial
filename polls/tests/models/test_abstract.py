from django.test import TestCase

from polls.models.abstract import NamedModel

class AbstractNamedModelTestCase(TestCase):
    """Test case for abstract base class NamedModel."""

    def test_str(self):
        """test choice str method."""
        name = "choice"
        instance = NamedModel(name=name)

        self.assertEqual(str(instance), name)
        self.assertEqual(instance.__str__(), name)

