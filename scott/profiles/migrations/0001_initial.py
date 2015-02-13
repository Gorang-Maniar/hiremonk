# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('candidate', models.ForeignKey(related_name=b'educations', to='profiles.Candidate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organisation_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('industry', models.CharField(max_length=3, choices=[(b'IT', b'Information Technology'), (b'EDU', b'Education'), (b'MKT', b'Marketing')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expectation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_type', models.CharField(max_length=1, choices=[(b'P', b'Part Time'), (b'F', b'Full Time')])),
                ('compensation', models.PositiveIntegerField()),
                ('currency', models.CharField(max_length=3, choices=[(b'USD', b'US Dollar'), (b'INR', b'Indian Rupee')])),
                ('duration', models.PositiveSmallIntegerField()),
                ('role', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('candidate', models.ForeignKey(related_name=b'expectations', to='profiles.Candidate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('candidate', models.ForeignKey(related_name=b'experiences', to='profiles.Candidate')),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('candidate', models.ForeignKey(related_name=b'portfolios', to='profiles.Candidate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=100)),
                ('summary', models.TextField(max_length=400)),
                ('user_type', models.CharField(max_length=3, choices=[(b'FRL', b'Freelancer'), (b'CMY', b'Company'), (b'MOD', b'Moderator')])),
                ('identity', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recommender_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('candidate', models.ForeignKey(related_name=b'recommendations', to='profiles.Candidate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_type', models.CharField(max_length=1, choices=[(b'L', b'Language'), (b'O', b'Organisational'), (b'T', b'Technical')])),
                ('skill', models.CharField(unique=True, max_length=30)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='location',
            name='profile',
            field=models.ForeignKey(related_name=b'locations', to='profiles.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employer',
            name='profile',
            field=models.OneToOneField(to='profiles.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='profile',
            field=models.ForeignKey(related_name=b'contacts', to='profiles.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidate',
            name='profile',
            field=models.OneToOneField(to='profiles.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidate',
            name='skills',
            field=models.ManyToManyField(related_name=b'candidates', to='profiles.Skill'),
            preserve_default=True,
        ),
    ]
