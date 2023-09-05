"""
The Greeting API Views

"""
# -*- coding: utf-8 -*-


import logging

from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from edx_rest_framework_extensions.auth.session.authentication import SessionAuthenticationAllowInactiveUser
from rest_framework import generics

from openedx.core.lib.api.authentication import BearerAuthenticationAllowInactiveUser
from openedx.core.lib.api.permissions import ApiKeyHeaderPermissionIsAuthenticated
from openedx.core.lib.api.view_utils import DeveloperErrorViewMixin
from openedx.features.greetings.models import Greeting
from openedx.features.greetings.serializers import GreetingSerializer

log = logging.getLogger(__name__)


class Greetings(DeveloperErrorViewMixin, generics.ListCreateAPIView):
    authentication_classes = (JwtAuthentication, BearerAuthenticationAllowInactiveUser,
                              SessionAuthenticationAllowInactiveUser,)
    permission_classes = (ApiKeyHeaderPermissionIsAuthenticated,)
    serializer_class = GreetingSerializer
    queryset = Greeting.objects.all()


    def get_queryset(self):
        query = super(Greetings, self).get_queryset()
        return query.filter(user=self.request.user)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
