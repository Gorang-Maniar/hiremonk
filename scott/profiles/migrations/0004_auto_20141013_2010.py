# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20141012_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='skills',
            field=models.ManyToManyField(related_name=b'candidates', to=b'profiles.Skill'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='profile',
            field=models.ForeignKey(related_name=b'contacts', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='education',
            name='candidate',
            field=models.ForeignKey(related_name=b'educations', to='profiles.Candidate'),
        ),
        migrations.AlterField(
            model_name='expectation',
            name='candidate',
            field=models.ForeignKey(related_name=b'expectations', to='profiles.Candidate'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='candidate',
            field=models.ForeignKey(related_name=b'experiences', to='profiles.Candidate'),
        ),
        migrations.AlterField(
            model_name='location',
            name='profile',
            field=models.ForeignKey(related_name=b'locations', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='candidate',
            field=models.ForeignKey(related_name=b'portfolios', to='profiles.Candidate'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='candidate',
            field=models.ForeignKey(related_name=b'recommendations', to='profiles.Candidate'),
        ),
    ]
