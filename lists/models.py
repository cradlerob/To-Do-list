from __future__ import unicode_literals

from django.db import models

class List( models.Model ):
    name = models.TextField( default = 'To-Do List' )

class Item(models.Model):
    text = models.TextField( default = '' ) ,
    list = models.ForeignKey( List ,default = None )

    def __str__(self):
        return self.text