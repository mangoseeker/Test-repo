from django.shortcuts import render
from django.http import HttpResponse

def index(requesr):
    return HttpResponse("Hey, you, you're finally awake!")