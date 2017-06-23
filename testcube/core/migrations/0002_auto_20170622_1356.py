# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 13:56
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resulterror',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases',
                                    to='core.Product'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='core.Team'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='analysis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='results', to='core.ResultAnalysis'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='results', to='core.ResultError'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='test_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='results',
                                    to='core.TestClient'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='test_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results',
                                    to='core.TestRun'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='testcase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results',
                                    to='core.TestCase'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs',
                                    to='core.Product'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='status',
            field=models.IntegerField(
                choices=[(-1, 'Pending'), (0, 'Passed'), (1, 'Failed'), (2, 'Analyzed'), (3, 'Abandoned')], default=-1),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='core.Team'),
        ),
    ]
