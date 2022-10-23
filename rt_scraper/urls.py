from django.urls import path
from .views import scraperPageView

urlpatterns = [
    path('scraper', scraperPageView, name='scraper'),
]
