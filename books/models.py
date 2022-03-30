from operator import mod
from pyexpat import model
from statistics import mode
from unicodedata import category, name
from django.db import models


from core.translate import dictionary

from django.contrib.auth import get_user_model

# setting user model
# this code provide migration tips to 
# USER_MODEL and provide ways to migrate default user of django
User = get_user_model()


class Category(models.Model):
    """
    Class to manage category

    """
    name = models.CharField('Cat', max_length=200)
    description = models.TextField('Cat', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class Folder(models.Model):
    """
    Model to retrive and manage folders to each book


    """

    name = models.CharField('Cat', max_length=200)
    description = models.TextField('Cat', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    """
    Model to retrive and manage authors to each book

    """
    name = models.CharField('', max_length=200)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    """
    Model to retrive and manage books

    """

    title = models.CharField('Cat', max_length=200)
    description = models.TextField('Cat')
    pages = models.PositiveIntegerField()

    # relationships
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    folder = models.ManyToManyField(Folder)

    def __str__(self) -> str:
        return self.title