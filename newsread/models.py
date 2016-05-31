
from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class NewsSource(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")

class Category(models.Model):
    title = models.CharField(max_length=200)

class Article(models.Model):
    headline = models.CharField(max_length=200)
    summary = models.TextField()
    #pub_date = models.DateTimeField(auto_now=False, auto_now_add=False,)
    link = models.CharField(max_length=500)

