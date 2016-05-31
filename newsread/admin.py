from django.contrib import admin

# Register your models here.
from newsread import models

admin.site.register(models.NewsSource),
admin.site.register(models.Category),
admin.site.register(models.Article),