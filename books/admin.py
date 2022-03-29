from django.contrib import admin

# Register your models here.
from .models import Author, Book, Category, Folder


# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Folder)