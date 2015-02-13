# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='location',
        ),
        migrations.AddField(
            model_name='education',
            name='city',
            field=models.CharField(default=b'New Delhi', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='country',
            field=models.CharField(default=b'India', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='state',
            field=models.CharField(default=b'Delhi', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expectation',
            name='state',
            field=models.CharField(default=b'Delhi', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default=b'Delhi', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='expectation',
            name='city',
            field=models.CharField(default=b'New Delhi', max_length=50),
        ),
        migrations.AlterField(
            model_name='expectation',
            name='country',
            field=models.CharField(default=b'India', max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(default=b'New Delhi', max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(default=b'India', max_length=50),
        ),
    ]
