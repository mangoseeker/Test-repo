from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    return HttpResponse("Hey, you, you're finally awake!")

def home(response):
    return render(response, "main/home.html", {})

def books(response):
    my_books = Book.objects.all()
    return render(response, "main/books.html", {"books": my_books})

def bookinfo(response):
    return render(response, "main/bookinfo.html", {})

def about(response):
    return render(response, "main/about.html", {})

def bookid(response, Book_id):
    print(Book_id)
    return render(response, "main/bookinfo.html", {})