from operator import mod
from unicodedata import name
from django.db import models


from core.translate import dictionary


class Category(models.Model):
    """
    Class to manage category

    """
    name = models.CharField('Cat', max_length=200)
    description = models.TextField('Cat')


class Folder(models.Model):
    """
    Model to retrive and manage folders to each book

    
    """

    name = models.CharField('Cat', max_length=200)
    description = models.TextField('Cat')

class Author(models.Model):
    name = models.CharField('', max_length=200)
    
class Book(models.Model):
    
    name = models.CharField('Cat', max_length=200)
    description = models.TextField('Cat')
    
    author = models.ForeignKey(Author)

