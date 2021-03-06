
from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']


