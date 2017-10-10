# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-09 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('status', models.IntegerField(choices=[(0, 'Wrong Answer'), (1, 'Accepted')])),
                ('source', models.TextField(default='')),
                ('first_solve', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdin', models.TextField()),
                ('stdout', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=64, unique=True)),
                ('question_body', models.TextField()),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('difficulty', models.IntegerField(choices=[(2, 'Easy'), (5, 'Medium'), (10, 'Hard')])),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinejudge.Category')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinejudge.Question'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinejudge.Question'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
