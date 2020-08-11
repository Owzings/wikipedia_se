from django.db import models

# Create your models here.


class Titre(models.Model):
    titre = models.CharField(max_length=200)