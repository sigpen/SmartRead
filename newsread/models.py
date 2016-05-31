from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class NewsSource(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=200)


class Article(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_at = models.DateTimeField()
    headline = models.CharField(max_length=200)
    summary = models.TextField()
    link = models.URLField()
