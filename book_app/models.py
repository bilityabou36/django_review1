from django.db import models
from library_app.models import Library
from django.core import validators as v

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    isbn = models.CharField(max_length=13,unique=True, validators=[v.MinLengthValidator(13)])
    genre = models.CharField()
    Library_id = models.ForeignKey(Library, on_delete=models.CASCADE)
    
def __str__(self):
    return self.title