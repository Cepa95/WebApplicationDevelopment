from django.db import models

# Create your models here.

class Predmeti(models.Model):
    IZBORNI = (('DA', 'da'), ('NE', 'ne'))
    name = models.CharField(max_length=50)
    kod = models.CharField(max_length=10)
    program = models.TextField(max_length=50,null=False)
    ects = models.IntegerField(null=False)
    sem_red = models.IntegerField(null=False)
    sem_izv = models.IntegerField(null=False)
    izborni = models.CharField(max_length=10, choices=IZBORNI)
