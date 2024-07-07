from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def authors(request):
    pass

