===========================
Django Book Collections
===========================

Book Collections is a Django app to manage receipts.

Quick start
===========

1. Add "booksPackage" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'booksPackage',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('books/', include('booksPackage.urls')),

3. Run ``python manage.py migrate`` to create the receipts models.

4. Start the development server and visit https://127.0.0.1:8080/books/books_json/