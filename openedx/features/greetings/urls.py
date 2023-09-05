"""
Greetings API URLs
"""


from django.urls import re_path

from .views import Greetings

urlpatterns = [
    re_path('', Greetings.as_view(), name='greetings'),
]
