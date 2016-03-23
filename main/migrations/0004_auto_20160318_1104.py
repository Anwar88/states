# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160317_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCapital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('capital_population', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital_population',
        ),
        migrations.RemoveField(
            model_name='state',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='longitude',
        ),
    ]
