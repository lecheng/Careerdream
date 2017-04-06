# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_datareport_line_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databactive',
            name='loss_rate',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='databactive',
            name='not_active_rate',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datacactive',
            name='loss_rate',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datacactive',
            name='not_active_rate',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=5),
            preserve_default=True,
        ),
    ]
