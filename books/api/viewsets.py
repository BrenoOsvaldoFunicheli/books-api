
from rest_framework import viewsets
from .serializers import FolderSerializer, AuthorSerializer, BookSerializer, CategorySerializer
from books.models import Author, Book, Category, Folder

from rest_framework import permissions
from rest_framework.response import Response


def filter_by_user(request, model, serializer, as_data=True):
    """
    This method manage the request user acess

    Args:
        request (_type_): _description_
        model (_type_): _description_
        serializer (_type_): _description_
        as_data (bool, optional): _description_. Defaults to True.

    """
    # get auth user to filter query
    authenticated_user = request.user 

    # filter only folder that belong to auth user
    queryset = model.objects.filter(owner=authenticated_user)

    serializer = serializer(queryset, many=True)

    # if True returns data of serializer as a dict 
    if as_data:
        return serializer.data
    
    return serializer


class FolderDefaultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing folder instances.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

    def list(self, request):
        
        # call generic function to get all
        return filter_by_user(request, Folder, FolderSerializer)



class AuthorDefaultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing folder instances.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()



class BookDefaultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing folder instances.
    """

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = BookSerializer

    queryset = Book.objects.all()

    def list(self, request):

        # call generic function to get all
        return filter_by_user(request, Book, BookSerializer)

        

class CategoryDefaultViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing folder instances.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request):


        # get auth user to filter query
        authenticated_user = request.user 

        # filter only folder that belong to auth user
        queryset = Category.objects.filter(owner=authenticated_user)

        serializer = CategorySerializer(queryset, many=True)

        return Response(serializer.data)
        