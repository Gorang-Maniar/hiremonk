# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20141012_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='expectation',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='expectation',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='expectation',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
