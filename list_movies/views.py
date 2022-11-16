from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def moviePageView(request):
    return render(request, 'list_movies/showmovies.html')