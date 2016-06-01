from django.db import models
from django.conf import settings
from django.utils.datetime_safe import datetime


class NewsSource(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    #category = models.ManyToManyField('Category')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    #source = models.ForeignKey('NewsSource', on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Article(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    summary = models.TextField(null=True)
    pub_date = models.DateTimeField(db_index=True)
    link = models.URLField()


    def __str__(self):
        return self.headline






# Create your models here.
