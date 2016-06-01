from django.test import TestCase

import datetime
import decimal

import random
from django.contrib.auth.models import User
from django.test import TestCase

from . import models


class SmartReadTestCase(TestCase):
    def test_smartread(self):
        cats = [models.Category('cat #{}'.format(i+1) for i in range(10))]
        #cats = [models.NewsSource('cat #{}'.format(i+1) for i in range(10))]

        n = 12
        for i in range(n):
            o = models.Category(

                title="SmartRead #{}".format(i + 1),

            )
            o.full_clean()
            o.save()

        self.assertEquals(models.Category.objects.count(), n)

# Create your tests here.
