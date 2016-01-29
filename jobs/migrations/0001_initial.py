# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('source', models.CharField(blank=True, max_length=255)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('application_type', models.CharField(blank=True, max_length=255)),
                ('response', models.CharField(blank=True, max_length=255)),
                ('active', models.BooleanField()),
                ('comments', models.TextField(blank=True, max_length=512)),
                ('job_type', models.CharField(choices=[('remote', 'Remote'), ('visa', 'Visa'), ('intern', 'Intern')], max_length=32)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.TextField(max_length=1024)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='jobs.JobApplication')),
            ],
        ),
    ]