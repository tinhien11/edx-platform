from factory.django import DjangoModelFactory
from openedx.features.greetings.models import Greeting


class UserCalendarSyncConfigFactory(DjangoModelFactory):
    """
    Factory class for SiteConfiguration model
    """
    class Meta:
        model = Greeting

    enabled = True
