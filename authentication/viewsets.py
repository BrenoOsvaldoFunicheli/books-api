
from rest_framework import viewsets, mixins

from .serializers import UserSerializer
from rest_framework import permissions


from django.contrib.auth import get_user_model

# setting user model
# this code provide migration tips to 
# USER_MODEL and provide ways to migrate default user of django
User = get_user_model()

# ViewSets define how to create and view the profile of user
class UserViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
