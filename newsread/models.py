from django.db import models
from django.conf import settings



class NewsSource(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="sources/")

class Category(models.Model):
    title = models.CharField(max_length=200)

class Article(models.Model):
    headline = models.CharField(max_length=200)
    summary = models.TextField()
    pub_date = models.DateTimeField()
    link = models.CharField(max_length=500)




# Create your models here.
