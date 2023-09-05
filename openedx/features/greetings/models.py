"""
Models for Greetings
"""


from django.contrib.auth.models import User
from django.db import models


class Greeting(models.Model):
    """
    Model to store greetings
    """
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
