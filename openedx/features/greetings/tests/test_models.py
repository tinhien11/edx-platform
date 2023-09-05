"""
Test GreetingModel
"""

from common.djangoapps.student.tests.factories import UserFactory
from django.test import TestCase
from ..tests.factories import GreetingFactory
from openedx.features.greetings.models import Greeting


class GreetingModelTest(TestCase):
    """
    Test case covering User Preference ORM model attributes and custom operations
    """
    def test_create_greetings(self):
        """Create greeting. """
        user = UserFactory.create()
        greeting = GreetingFactory.create(user=user, content="hello")
        assert greeting.user == user
        assert greeting.content == "hello"

    def test_retire_greetings_by_user(self):
        user = UserFactory.create()
        GreetingFactory.create(user=user, content="hello")
        GreetingFactory.create(user=user, content="hi")
        assert len(Greeting.objects.filter(user_id=user.id)) == 2
        # Delete the tags by user value. Ensure the rows no longer exist.
        Greeting.objects.filter(user=user).delete()
        assert len(Greeting.objects.filter(user_id=user.id)) == 0
