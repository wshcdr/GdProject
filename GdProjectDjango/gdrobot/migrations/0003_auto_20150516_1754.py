# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdrobot', '0002_auto_20150516_1732'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Organzation',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.DeleteModel(
            name='UploadFiles',
        ),
    ]
