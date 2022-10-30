from django.urls import path

from . import views

urlpatterns = [
    path("books_json/", views.books_json, name='books_json'),
]