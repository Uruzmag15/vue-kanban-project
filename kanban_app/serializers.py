from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Card


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class CardSerializer(serializers.ModelSerializer):
    # creator = UserSerializer()

    class Meta:
        model = Card
        fields = ('id', 'status', 'text', 'date')
