from django.urls import path
from .views import *

urlpatterns = [
    path('', listPageView, name='index'),
    path('changeRank/<int:id>/<str:pos>/', changeRank, name='changeRank'),
    path('editMovie/<int:id>/', editMovie, name="editMovie"),
    path("deleteMovie/<int:id>/", deleteMovie, name="deleteMovie"),
]