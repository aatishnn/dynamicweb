# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-22 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenterlight', '0014_dclsectionpromopluginmodel'),
        ('datacenterlight', '0014_dclnavbarpluginmodel_language_dropdown'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dclsectionpromopluginmodel',
            old_name='center_on_mobile',
            new_name='text_center',
        ),
    ]
