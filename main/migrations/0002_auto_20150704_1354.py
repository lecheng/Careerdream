# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='feedback',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='hrfeedback',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='interviewtime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='面试时间'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='isinterview',
            field=models.BooleanField(verbose_name='面试', default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='ip',
            field=models.CharField(blank=True, null=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='login_num',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='paper_plane_num',
            field=models.IntegerField(verbose_name='收到的纸飞机', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='contacts',
            field=models.CharField(blank=True, null=True, max_length=50, verbose_name='联系人'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='interaddress',
            field=models.CharField(blank=True, null=True, max_length=100, verbose_name='面试地点'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='memo',
            field=models.CharField(blank=True, null=True, max_length=100, verbose_name='备注'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='phone',
            field=models.CharField(blank=True, null=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.ForeignKey(null=True, to='main.Resume'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(max_length=2, choices=[('SU', 'Submitted'), ('AC', 'Accepted'), ('RJ', 'Rejected'), ('RP', 'Reposted'), ('RE', 'Read'), ('TO', 'Timeout/OffLine'), ('IN', 'Interview')], default='SU'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='acceptnum',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='ip',
            field=models.CharField(blank=True, null=True, max_length=30),
            preserve_default=True,
        ),
    ]
