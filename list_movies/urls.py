from django.urls import path
from .views import moviePageView

urlpatterns = [
    path('', moviePageView, name='list'),
]
