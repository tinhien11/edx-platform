"""
Greeting API Serializers.  Representing greeting catalog data
"""

from rest_framework import serializers
from .models import Greeting


class GreetingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Greeting
        fields = '__all__'
