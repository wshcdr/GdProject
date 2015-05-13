# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackAdmin', '0002_auto_20150512_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organzation',
            name='orgrhomephone',
            field=models.CharField(db_column='orgRHomephone', null=True, blank=True, max_length=45),
        ),
    ]
