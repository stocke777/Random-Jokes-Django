from django.db import models

# Create your models here.
class JokeList(models.Model):
    content=models.TextField()