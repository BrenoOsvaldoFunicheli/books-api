
from unicodedata import category
from rest_framework import serializers

from rest_flex_fields import FlexFieldsModelSerializer


from books.models import Folder, Author, Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        exclude = ['owner']
        
        

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Folder
        exclude = ['owner']
        

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Author
        fields = '__all__'
        

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    folder = FolderSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model =  Book
        exclude = ['owner']


        
        