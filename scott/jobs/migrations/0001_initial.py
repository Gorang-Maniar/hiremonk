# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('benefit_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'[0-9]*$', b'Only numbers are allowed')])),
                ('work', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'[0-9]*$', b'Only numbers are allowed')])),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('overview', models.TextField()),
                ('job_type', models.CharField(max_length=1, choices=[(b'P', b'Part Time'), (b'F', b'Full Time')])),
                ('industry', models.CharField(max_length=3, choices=[(b'IT', b'Information Technology'), (b'EDU', b'Education'), (b'MKT', b'Marketing')])),
                ('category', models.CharField(max_length=3, choices=[(b'SW', b'Software'), (b'RnD', b'Research and Development')])),
                ('compensation', models.PositiveIntegerField()),
                ('currency', models.CharField(max_length=3, choices=[(b'USD', b'US Dollar'), (b'INR', b'Indian Rupee')])),
                ('role', models.CharField(max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('candidates', models.ManyToManyField(related_name=b'jobs_candidates', to='profiles.Candidate')),
                ('employer', models.ForeignKey(related_name=b'jobs_employer', to='profiles.Employer')),
                ('required_skills', models.ManyToManyField(related_name=b'jobs', to='profiles.Skill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(b'[0-9]*$', b'Only numbers are allowed')])),
                ('job', models.ForeignKey(related_name=b'job_locations', to='jobs.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='job',
            field=models.ForeignKey(related_name=b'job_contacts', to='jobs.Job'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='benefit',
            name='job',
            field=models.ForeignKey(related_name=b'benefits', to='jobs.Job'),
            preserve_default=True,
        ),
    ]
