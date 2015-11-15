# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virusList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virus',
            name='size_KB',
            field=models.DecimalField(default=0, max_digits=128, decimal_places=5),
        ),
    ]
