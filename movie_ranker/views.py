from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Max

# Create your views here.
def listPageView(request):
    if request.method == "POST":
        movie, created = Movie.objects.get_or_create(movie_title=request.POST["movie_title"])
        if Movie.objects.all().aggregate(Max("ranking"))['ranking__max'] != None:
            newRank = Movie.objects.all().aggregate(Max("ranking"))['ranking__max'] + 1
        else:
            newRank = 1
        movie.ranking = newRank
        movie.genre.set(request.POST.getlist('genre'))
        movie.box_office_rev = request.POST["box_office_revenue"]
        movie.rating = Rating.objects.get(id = request.POST["rating"])
        movie.runtime = (str(request.POST["runtime-hours"]) + ":" + str(request.POST['runtime-minutes']))
        movie.save()
        return redirect('index')
    else:
        context = {
            'movies' : Movie.objects.all().order_by('ranking'),
            'genres' : Genre.objects.all(),
            'ratings': Rating.objects.all()
        }   
        return render(request, 'index.html', context)

def editMovie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        movie.movie_title = request.POST["movie_title"]
        movie.genre.set(request.POST.getlist('genre'))
        movie.box_office_rev = request.POST["box_office_revenue"]
        movie.rating = Rating.objects.get(id=request.POST["rating"])
        movie.runtime = (str(request.POST["runtime-hours"]) + ":" + str(request.POST['runtime-minutes']))
        movie.save()
        return redirect('index')
    else:
        timedelta_str = str(movie.runtime)
        hours = timedelta_str[0:timedelta_str.find(":")]
        minutes = timedelta_str[timedelta_str.find(":")+1:timedelta_str.find(":")+3]
        context = {
            'movie': movie,
            'runtime': {'hours': hours, 'minutes': minutes},
            'genres': Genre.objects.all(),
            'ratings': Rating.objects.all()
        }
        return render(request, 'editMovie.html', context)

def changeRank(request, id, pos):
    movieClicked = Movie.objects.get(id=id)
    try:
        if pos == 'up':
            movieDisplaced = Movie.objects.get(ranking=movieClicked.ranking - 1)
        else:
            movieDisplaced = Movie.objects.get(ranking=movieClicked.ranking + 1)
        if (pos == 'up') and (movieClicked.ranking > 1):
            movieClicked.ranking = movieClicked.ranking - 1
            movieDisplaced.ranking = movieDisplaced.ranking + 1
        elif pos == 'down':
            movieClicked.ranking = movieClicked.ranking + 1
            movieDisplaced.ranking = movieDisplaced.ranking - 1
        movieDisplaced.save()
        movieClicked.save()
        return redirect('index')
    except:
        return redirect('index')
    
def deleteMovie(request, id):
    data = Movie.objects.get(id = id)
    moviesAfter = Movie.objects.filter(ranking__gt=data.ranking)
    for movie in moviesAfter:
        movie.ranking = movie.ranking - 1
        movie.save()
    data.delete()

    return redirect('index')

def addMovieView(request):
    return HttpResponse('Form that allows users to manually input details about a movie. Writes those details to the database. Include links to scraper and list movies page.')

def scraperPageView(request):
    return HttpResponse('Takes a rotten tomatoes link as an input, scrapes the site, and assembles a dictionary of information gained from scraping. Writes info from that dictionary to our database.')
