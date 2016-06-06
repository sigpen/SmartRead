from django.db import models

from django.conf import settings
from django.utils.datetime_safe import datetime


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class NewsSource(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title


class Article(models.Model):
    source = models.ForeignKey(NewsSource)
    category = models.ForeignKey(Category)
    headline = models.CharField(max_length=200)
    summary = models.TextField(null=True)
    pub_date = models.DateTimeField()
    link = models.URLField()

    def __str__(self):
        return self.headline
