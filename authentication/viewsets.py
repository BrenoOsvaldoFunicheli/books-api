
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins

from .serializers import UserSerializer
from rest_framework import permissions


# ViewSets define how to create and view the profile of user
class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
