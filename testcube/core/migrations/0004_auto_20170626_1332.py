# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0003_auto_20170622_1431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testcase',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='testresult',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='resultanalysis',
            name='reason',
            field=models.IntegerField(
                choices=[(0, 'Product defect'), (1, 'Testcase defect'), (2, 'Environment issue'), (3, 'Other')],
                default=0),
        ),
    ]
