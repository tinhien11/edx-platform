""" Tests for the Greetings API """


from common.djangoapps.student.tests.factories import UserFactory
from openedx.features.greetings.models import Greeting
from django.test import TestCase

TEST_PASSWORD = 'test'


class TestGreetingsAPI(TestCase):
    """ Tests for the Greetings API """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()
        self.user = UserFactory(password=TEST_PASSWORD)

    def test_success_create_a_greeting(self):
        assert Greeting.objects.count() == 0
        Greeting.objects.create(user=self.user, content='hello')
        assert Greeting.objects.count() == 1
