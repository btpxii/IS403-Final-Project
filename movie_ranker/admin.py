from django.contrib import admin
from .models import *

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(Actor_Movie)

# Register your models here.
