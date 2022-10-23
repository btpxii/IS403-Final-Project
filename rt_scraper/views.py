from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def scraperPageView(request):
    return HttpResponse('Takes a rotten tomatoes link as an input, scrapes the site, and assembles a dictionary of information gained from scraping. Writes info from that dictionary to our database.')