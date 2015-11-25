# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virusList', '0004_virus_detection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virus',
            name='Detection',
            field=models.TextField(),
        ),
    ]
