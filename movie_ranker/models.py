from django.db import models

# Create your models here.
# class Actor(models.Model):
#     actor_first_name = models.CharField(max_length=30)
#     actor_last_name = models.CharField(max_length=30)

#     # def save(self):
#     #     self.actor_first_name = self.actor_first_name.upper()
#     #     self.actor_last_name = self.actor_last_name.upper()
#     #     super(Actor, self).save()

#     class Meta:
#         db_table = 'Actor'
   
#     def __str__(self):
#         return (self.actor_first_name + " " + self.actor_last_name)
   
class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Genre'

    def __str__(self):
        return (self.genre_name)

class Rating(models.Model):
    rating_name = models.CharField(max_length=50)
    rating_meaning = models.CharField(max_length=250)

    class Meta:
        db_table = 'Rating'

    def __str__(self):
        return (self.rating_name)

class Movie(models.Model):
    movie_title = models.CharField(max_length = 200)
    ranking = models.IntegerField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    box_office_rev = models.FloatField(null=True, blank=True)
    runtime = models.DurationField(null=True, blank=True)
    rating = models.ForeignKey(Rating, blank=True, null=True, on_delete=models.CASCADE)
    # actors = models.ManyToManyField(Actor, blank=True, through="actor_movie")

    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return (self.movie_title)

# class Actor_Movie(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
#     char_name = models.CharField(max_length=100, blank=True)

#     class Meta:
#         db_table = 'Actor_Movie'

#     def __str__(self):
#         return (self.actor.actor_first_name + ' ' + self.actor.actor_last_name + ' as ' + self.char_name)
