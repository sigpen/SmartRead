from django.contrib import admin


from newsread import models

admin.site.register(models.NewsSource),
admin.site.register(models.Category),
admin.site.register(models.Article),
