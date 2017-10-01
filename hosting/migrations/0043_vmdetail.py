# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-09-24 18:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hosting', '0042_hostingorder_subscription_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='VMDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vm_id', models.IntegerField(default=0)),
                ('disk_size', models.FloatField(default=0.0)),
                ('cores', models.FloatField(default=0.0)),
                ('memory', models.FloatField(default=0.0)),
                ('configuration', models.CharField(default='', max_length=25)),
                ('ipv4', models.TextField(default='')),
                ('ipv6', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('terminated_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]