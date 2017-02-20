from __future__ import unicode_literals

from django.db import models


class List(models.Model):
    name = models.TextField(default='To-Do List')


    def __str__(self):
        return self.name


class Item(models.Model):
    text_item = models.CharField(max_length=70,default='item')
    list = models.ForeignKey(List)


    def __str__(self):
        return self.text_item
