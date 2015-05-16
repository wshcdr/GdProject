# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdrobot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.AlterModelOptions(
            name='organzation',
            options={},
        ),
        migrations.AlterModelOptions(
            name='register',
            options={},
        ),
        migrations.AlterModelTable(
            name='member',
            table=None,
        ),
        migrations.AlterModelTable(
            name='organzation',
            table=None,
        ),
        migrations.AlterModelTable(
            name='register',
            table=None,
        ),
    ]
