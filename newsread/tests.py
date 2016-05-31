import datetime

from django.test import TestCase
from newsread import models

class NewsreadTestCase(TestCase):
    def test_news_source(self):
        #source = [models.NewsSource("News Source #{}".format(i + 1)) for i in range(5)]
        n = 12
        for i in range(n):
            o = models.NewsSource(
                title="Source #{}".format(i + 1),
                image="tday"
            )
            o.full_clean()
            o.save()

        self.assertEquals(models.NewsSource.objects.count(), n)