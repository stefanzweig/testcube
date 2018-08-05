# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 07:44
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0010_auto_20171009_1634'),
        ('runner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunVariables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(default=None, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('test_run',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='run_variables',
                                      to='core.TestRun')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(-1, 'Pending'), (0, 'Sent'), (1, 'Error')], default=-1),
        ),
    ]
