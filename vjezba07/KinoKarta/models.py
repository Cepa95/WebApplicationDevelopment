from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projekcija(models.Model):
    movie = models.CharField(max_length=50)
    time = models.TimeField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.movie} {self.time} {self.capacity}'


class Karta(models.Model):
    seat = models.IntegerField()
    movie = models.ForeignKey(Projekcija, blank = True, null = True, on_delete = models.CASCADE)
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.seat, self.movie, self.user)