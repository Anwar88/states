# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160318_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.ForeignKey(to='main.State', null=True),
        ),
    ]
