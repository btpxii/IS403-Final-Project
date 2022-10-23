from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    return HttpResponse('Home page goes here. Include links to scraper and manual input forms. Display all movies from out database, in user-defined order. Allow users to change movie ranking by dragging and dropping.')