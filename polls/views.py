from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey, you, you're finally awake!")

def home(response):
    return render(response, "main/home.html", {})

def books(response):
    return render(response, "main/books.html", {})