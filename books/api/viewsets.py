
import re
from telnetlib import STATUS
from rest_framework import viewsets
from .serializers import FolderSerializer, AuthorSerializer, BookSerializer, CategorySerializer
from books.models import Author, Book, Category, Folder

from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.db.models import Q

from books.api.pagination import LargeResultsSetPagination


def delete_public(request, model, pk=None):
    """This method manage delete action 
    to prevente that another user delete a public object.
    This funcition is to generalize action

    Args:
        request (_type_): DRF request 
        model (_type_): Django model to query
        pk (_type_, optional): primary key of objet to delete

    Returns:
        _type_: _description_
    """

    # get user
    authenticated_user = request.user

    # the user can see only he's owner or if category is public
    instance = model.objects.filter(owner=authenticated_user, pk=pk)

    info = instance.delete()

    if instance:
        return Response({'response': {'isDelete': True, 'info': info}}, status=200)
    else:
        return Response({'response': {'isDelete': False, 'info': "You can't delete this object"}}, status=500)


class FolderDefaultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing folder instances.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

    def get_queryset(self):

        authenticated_user = self.request.user

        # the user can see only he's owner or if category is public
        return Folder.objects.filter(Q(owner=authenticated_user) | Q(public=True))

    def destroy(self, request, pk=None):
        """This method prevent that public folders 
        will be delete for another user

        Args:
            request (_type_): _description_
            pk (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return delete_public(request,Folder, pk)


class AuthorDefaultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing author instances.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookDefaultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing books instances.
    """

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = BookSerializer

    queryset = Book.objects.all()

    def get_queryset(self):

        # filter by user ownership
        authenticated_user = self.request.user

        return Book.objects.filter(owner=authenticated_user)


class CategoryDefaultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories instances.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    # example to diferent pagination
    pagination_class = LargeResultsSetPagination


    def get_queryset(self):

        # filter by user ownership
        authenticated_user = self.request.user

        # the user can see only he's owner or if category is public
        return Category.objects.filter(Q(owner=authenticated_user) | Q(public=True))

    def destroy(self, request, pk=None):
        
        # prevente unauthtorized delete
        return delete_public(request, Category, pk)
