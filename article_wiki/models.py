from django.db import models
from titre_wiki.models import Titre

# Create your models here.
class Article(models.Model):
    title = models.ForeignKey(Titre, blank=True, null=True, on_delete=models.CASCADE,)
    content = models.CharField(max_length=20000)