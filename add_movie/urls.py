from django.urls import path
from .views import addMovieView

urlpatterns = [
    path('addmovie', addMovieView, name='addmovie'),
]
