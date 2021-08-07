from django.urls import path

from . import views
# home/ creating new path for home.html, path is home/home now
urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('home/', views.home, name="home"),
    path('bookinfo/', views.bookinfo, name="bookinfo"),
    path('about/', views.about, name="about"),
    path("bookinfo/<int:Book_id>/", views.bookinfo, name="bookinfo"),
    path('delete/(?P<m>[0-9]+)/', views.book_delete, name='book_delete'),
    path('create/', views.create, name="create"),
    path('savecreate', views.create_book, name="create_book")
]
# r'^delete/(?P<pk>[0-9]+)/$'