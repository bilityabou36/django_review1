from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from django.core.serializers import serialize
import json

# Create your views here.
# def hello_django(request):
#     return JsonResponse({"greet":"HELLO DJANGO"})

class All_Books(APIView):
    def get(self, request):
        query_all_books = Book.objects.all()
        print(query_all_books)
        formatted_books = json.loads(serialize("json", query_all_books))
        for idx, book in enumerate(query_all_books):
            formatted_books[idx]["fields"]["members"] = json.loads(
                serialize("json", book.members.all())
            )
        return Response(formatted_books)
    