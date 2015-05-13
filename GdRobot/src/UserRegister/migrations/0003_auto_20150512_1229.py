# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserRegister', '0002_organzation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organzation',
            old_name='orglrhomephoe',
            new_name='orglrhomephone',
        ),
        migrations.RenameField(
            model_name='organzation',
            old_name='orgrhomephoe',
            new_name='orgrhomephone',
        ),
        migrations.RemoveField(
            model_name='organzation',
            name='revenueOneyearAgo',
        ),
        migrations.RemoveField(
            model_name='organzation',
            name='revenueThreeyearAgo',
        ),
        migrations.RemoveField(
            model_name='organzation',
            name='revenueTwoyearAgo',
        ),
        migrations.AddField(
            model_name='organzation',
            name='revenueoneyearago',
            field=models.IntegerField(blank=True, db_column='revenueOneyearAgo', null=True),
        ),
        migrations.AddField(
            model_name='organzation',
            name='revenuethreeyearago',
            field=models.IntegerField(blank=True, db_column='revenueThreeyearAgo', null=True),
        ),
        migrations.AddField(
            model_name='organzation',
            name='revenuetwoyearago',
            field=models.IntegerField(blank=True, db_column='revenueTwoyearAgo', null=True),
        ),
    ]
