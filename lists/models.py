from __future__ import unicode_literals

from django.db import models


class List(models.Model):
    name = models.TextField(default='To-Do List')

    def __str__(self):
        return self.name


class Item(models.Model):
    text_item = models.CharField(default='N'),
    list = models.ForeignKey(List)
