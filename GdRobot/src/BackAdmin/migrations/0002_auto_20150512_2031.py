# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organzation',
            name='orglrhomephone',
            field=models.CharField(null=True, max_length=45, blank=True, db_column='orgLRHomephone'),
        ),
    ]
