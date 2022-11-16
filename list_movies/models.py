from django.db import models

# Create your models here.
class actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(actor, self).save()
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)     
    def __str__(self):
        return (self.full_name)
   
        
class movie(models.Model):
    tile = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 20)
    box_office_rev = models.FloatField()
    runtime = models.TimeField()
    audience_rating = models.FloatField()
    actors = models.ManyToManyField(actor, blank=True)
    def save(self):
        self.audience_rating = round(self.audience_rating,4)
        super(movie, self).save()