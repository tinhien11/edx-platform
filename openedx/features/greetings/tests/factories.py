from factory.django import DjangoModelFactory
from openedx.features.greetings.models import Greeting


class GreetingFactory(DjangoModelFactory):
    """
    Factory class for SiteConfiguration model
    """
    class Meta:
        model = Greeting
