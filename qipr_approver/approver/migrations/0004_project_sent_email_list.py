# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approver', '0003_auto_20170124_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sent_email_list',
            field=models.ManyToManyField(related_name='emailed_for_projects', to='approver.Person'),
        ),
    ]