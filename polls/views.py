from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Hey, you, you're finally awake!")

def home(response):
    return render(response, "main/home.html", {})

def books(response):
    my_books = Book.objects.all()
    return render(response, "main/books.html", {"books": my_books})

def bookinfo(response, Book_id):
    book = Book.objects.get(id=Book_id)
    print(book)
    return render(response, "main/bookinfo.html", {"book": book})

def about(response):
    return render(response, "main/about.html", {})

def bookid(response, Book_id):
    print(Book_id)
    return render(response, "main/bookinfo.html", {})

def book_delete(request, m):
    print(m)
    book = Book.objects.get(id=m)

    if request.method == 'POST':
        book.delete()
        return redirect('/')

    return render(request, 'main/books.html', {'book': book})

def create(response):
    return render(response, "main/create.html")

def create_book(request):
    if request.method == "POST":
        print(request.POST['name'])
        author = Author(name=request.POST['aftername'])
        author.save()
        book = Book(name=request.POST['name'], year=request.POST['year'], author = author)
        print(request.POST['aftername'])
        print(book.name)
        author.save()
        book.save()


    else:
        book = Book()
    return redirect('/books/')
