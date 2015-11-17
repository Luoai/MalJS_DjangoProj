# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virusList', '0002_auto_20151115_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='virus',
            old_name='url',
            new_name='VirusTotal_link',
        ),
    ]
