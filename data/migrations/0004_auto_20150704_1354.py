# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150608_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='datareg',
            name='b_account',
            field=models.IntegerField(blank=True, null=True, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datareg',
            name='b_active_singin',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dataposition',
            name='aver_position',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dataposition',
            name='loss_aver',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dataresume',
            name='c_delivery',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dataresume',
            name='pos_aver',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
