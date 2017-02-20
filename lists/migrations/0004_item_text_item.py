# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text_item',
            field=models.CharField(default='item', max_length=70),
        ),
    ]
