from django.shortcuts import render
from .models import Book, User

def home(request):
    return render(request, 'home.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def authors(request):
    pass

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password']
        new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)