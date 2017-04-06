# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentData',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('company_id', models.CharField(null=True, blank=True, max_length=10)),
                ('coname', models.CharField(null=True, blank=True, max_length=100)),
                ('company_email', models.CharField(null=True, blank=True, max_length=100)),
                ('datetime', models.DateField(null=True, blank=True)),
                ('score', models.IntegerField(null=True, blank=True, default=0)),
                ('resume_rate', models.CharField(null=True, blank=True, max_length=10)),
                ('tucao_count', models.IntegerField(null=True, blank=True, default=0)),
                ('support_count', models.IntegerField(null=True, blank=True, default=0)),
                ('date_comment', models.IntegerField(null=True, blank=True, default=0)),
                ('total_comment', models.IntegerField(null=True, blank=True, default=0)),
                ('user_count', models.IntegerField(null=True, blank=True, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DailyPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateField(null=True, blank=True)),
                ('c_read', models.IntegerField(null=True, blank=True)),
                ('c_forward', models.IntegerField(null=True, blank=True)),
                ('c_mark', models.IntegerField(null=True, blank=True)),
                ('c_expire', models.IntegerField(null=True, blank=True)),
                ('c_works', models.IntegerField(null=True, blank=True)),
                ('average_application', models.FloatField(blank=True, default='0')),
                ('daily_refresh', models.IntegerField(blank=True, default=0)),
                ('b_down', models.IntegerField(null=True, blank=True, default=0)),
                ('position_due', models.IntegerField(null=True, blank=True, default=0)),
                ('date_aver', models.FloatField(null=True, blank=True, default=0)),
                ('match_total', models.IntegerField(null=True, blank=True, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateTimeField(null=True, blank=True)),
                ('b_ratio', models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)),
                ('c_ratio', models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataBactive',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateField(null=True, blank=True)),
                ('user_active', models.IntegerField(null=True, blank=True)),
                ('user_loss', models.IntegerField(null=True, blank=True)),
                ('loss_rate', models.IntegerField(null=True, blank=True)),
                ('return_rate', models.IntegerField(null=True, blank=True)),
                ('not_active', models.IntegerField(null=True, blank=True)),
                ('not_active_rate', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataCactive',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateField(null=True, blank=True)),
                ('user_active', models.IntegerField(null=True, blank=True)),
                ('user_loss', models.IntegerField(null=True, blank=True)),
                ('loss_rate', models.IntegerField(null=True, blank=True)),
                ('return_rate', models.IntegerField(null=True, blank=True)),
                ('not_active', models.IntegerField(null=True, blank=True)),
                ('not_active_rate', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateField(null=True, blank=True)),
                ('position_total', models.IntegerField(null=True, blank=True)),
                ('add_position', models.IntegerField(null=True, blank=True)),
                ('aver_position', models.IntegerField(null=True, blank=True)),
                ('loss_add', models.IntegerField(null=True, blank=True)),
                ('loss_aver', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataReg',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateField(null=True, blank=True)),
                ('c_user_reg', models.IntegerField(null=True, blank=True)),
                ('b_total', models.IntegerField(null=True, blank=True)),
                ('b_active_reg', models.IntegerField(null=True, blank=True)),
                ('b_passive_reg', models.IntegerField(null=True, blank=True)),
                ('c_reg_total', models.IntegerField(null=True, blank=True)),
                ('b_reg_total', models.IntegerField(null=True, blank=True)),
                ('b_active_total', models.IntegerField(null=True, blank=True)),
                ('b_passive_total', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataReport',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateTimeField(null=True, blank=True)),
                ('total_reg', models.IntegerField(null=True, blank=True)),
                ('b_user_reg', models.IntegerField(null=True, blank=True)),
                ('c_user_reg', models.IntegerField(null=True, blank=True)),
                ('distinct_application_user', models.IntegerField(null=True, blank=True)),
                ('total_application', models.IntegerField(null=True, blank=True)),
                ('total_job', models.IntegerField(null=True, blank=True)),
                ('company_ip', models.IntegerField(null=True, blank=True, default='0')),
                ('b_ip', models.IntegerField(null=True, blank=True, default='0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataResume',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateField(null=True, blank=True)),
                ('pos_aver', models.IntegerField(null=True, blank=True)),
                ('resume_total', models.IntegerField(null=True, blank=True)),
                ('new_delivery', models.IntegerField(null=True, blank=True)),
                ('c_delivery', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Active',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateField(null=True, blank=True)),
                ('day_active', models.IntegerField(null=True, blank=True)),
                ('week_active', models.IntegerField(null=True, blank=True)),
                ('month_active', models.IntegerField(null=True, blank=True)),
                ('week_inactive', models.CharField(null=True, blank=True, max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
