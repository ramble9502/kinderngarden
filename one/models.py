# -*- coding: UTF-8 -*-
from django.db import models
import datetime
# Create your models here.


class jktree(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    time = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return self.title


class mmready(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    time = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return self.title


class Mombaby(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    time = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return self.title
