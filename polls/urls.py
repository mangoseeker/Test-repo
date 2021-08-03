from django.urls import path

from . import views
# home/ creating new path for home.html, path is home/home now
urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('home/', views.home, name="home"),

]