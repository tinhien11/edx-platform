"""Tests of openedx.features.greetings.views"""

from django.test.client import Client
from django.urls import reverse
from common.djangoapps.student.tests.factories import TEST_PASSWORD, UserFactory
from rest_framework.test import APITestCase


class TestGreetingView(APITestCase):

    def setUp(self):
        super().setUp()
        self.user = UserFactory.create()
        self.client = Client()
        self.url = reverse(
            'api_greetings:greetings',
        )

    def test_url(self):
        """
        Test that the url hasn't changed
        """
        assert self.url == '/api/greetings/'

    def test_create_greeting(self):
        """
        Test that the api create greeting
        """
        self.client.login(username=self.user.username, password=TEST_PASSWORD)
        # the endpoint should return a 200 if all goes well
        response = self.client.post(self.url,  {'content': 'hello'})
        assert response.status_code == 201

        expected_payload = {'content': 'hello'}
        assert expected_payload['content'] == response.data['content']

    def test_list_greeting(self):
        """
        Test that the api returns greetings list
        """
        self.client.login(username=self.user.username, password=TEST_PASSWORD)
        response = self.client.get(self.url)
        print(response.data)
        assert response.status_code == 200

        expected_payload = {'results': [], 'count': 0}
        assert expected_payload['results'] == response.data['results']
        assert expected_payload['count'] == response.data['count']


    def test_create_greeting_no_user(self):
        """
        Test that the endpoint returns a 401 if there is no user signed in
        """
        # the endpoint should return a 401 because the user is not logged in
        response = self.client.post(self.url, {'content': 'hello'})
        assert response.status_code == 401
