from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addMovieView(request):
    return HttpResponse('Form that allows users to manually input details about a movie. Writes those details to the database. Include links to scraper and list movies page.')