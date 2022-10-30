from django.shortcuts import render

from django.http import JsonResponse
from .models import Book


def books_json(request):
    results = {
        "books": [],
    }

    for book in Book.objects.all():
        line = {
            'name': book.name,
            'page': book.page
        }

        results["books"].append(line)

    return JsonResponse(results)
