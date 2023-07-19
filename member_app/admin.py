from django.contrib import admin
from .models import  Library, Book, Members
admin.site.register([Members, Book, Library])

# Register your models here.
