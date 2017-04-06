# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import main.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('unique_id', models.CharField(max_length=100, default=uuid.uuid4)),
                ('status', models.CharField(max_length=2, default='SU', choices=[('SU', 'Submitted'), ('AC', 'Accepted'), ('RJ', 'Rejected'), ('RP', 'Reposted'), ('RE', 'Read'), ('TO', 'Timeout/OffLine')])),
                ('isreposted', models.BooleanField(default=False)),
                ('isread', models.BooleanField(default=False)),
                ('isrejected', models.BooleanField(default=False)),
                ('isupdated', models.BooleanField(default=False)),
                ('istimeout', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('reposttime', models.DateTimeField(blank=True, null=True)),
                ('readtime', models.DateTimeField(blank=True, null=True)),
                ('rejecttime', models.DateTimeField(blank=True, null=True)),
                ('accepttime', models.DateTimeField(blank=True, null=True)),
                ('rejected', models.IntegerField(blank=True, null=True)),
                ('timeouttime', models.DateTimeField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('is_new', models.NullBooleanField(default=True)),
                ('downtime', models.DateTimeField(blank=True, null=True)),
                ('olresume', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('articles', models.TextField(blank=True, max_length=5000)),
                ('smallimg', models.ImageField(verbose_name='缩略图', blank=True, upload_to='titleimg')),
                ('titleimg', models.ImageField(blank=True, upload_to='titleimg')),
                ('category', models.CharField(blank=True, max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('click', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='证书名', blank=True, null=True, max_length=50)),
                ('is_activated', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('ment_companyid', models.CharField(null=True, max_length=100)),
                ('comments', models.TextField(blank=True, max_length=200)),
                ('comm_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('position', models.CharField(max_length=2, default='s', choices=[('s', 'support'), ('o', 'opposition')])),
                ('quote_who', models.CharField(null=True, max_length=100)),
                ('anonymous', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('unique_id', models.CharField(unique=True, max_length=100, default=uuid.uuid4)),
                ('coname', models.CharField(blank=True, max_length=50)),
                ('copwd', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('latitude', models.DecimalField(blank=True, null=True, decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(blank=True, null=True, decimal_places=7, max_digits=10)),
                ('scale', models.CharField(blank=True, max_length=20)),
                ('domain', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=5000)),
                ('website', models.URLField(blank=True)),
                ('benefit', models.CharField(verbose_name='公司福利', blank=True, max_length=100)),
                ('logo', models.ImageField(blank=True, upload_to='logo')),
                ('register_date', models.DateTimeField(blank=True, null=True)),
                ('last_login_date', models.DateTimeField(blank=True, null=True)),
                ('is_vip', models.BooleanField(default=False)),
                ('is_activated', models.BooleanField(default=False)),
                ('company_score', models.IntegerField(default=0)),
                ('company_oldscore', models.IntegerField(default=0)),
                ('uber_benefit', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EducationExpericence',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('school', models.CharField(verbose_name='学校名称', max_length=50)),
                ('major', models.CharField(verbose_name='所学专业', max_length=50)),
                ('gpa_score', models.FloatField(blank=True, null=True)),
                ('gpa_total', models.FloatField(blank=True, null=True)),
                ('course', models.CharField(verbose_name='所修课程', blank=True, null=True, max_length=100)),
                ('degree', models.CharField(verbose_name='所获学位', max_length=1, default='B', choices=[('J', 'Junior college'), ('B', 'Bachelor'), ('M', 'Master'), ('P', 'PhD'), ('R', 'Reading')])),
                ('grade', models.CharField(verbose_name='在读年级', blank=True, null=True, max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_activated', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('img', models.ImageField(blank=True, upload_to='./img')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('category', models.CharField(verbose_name='标签', blank=True, max_length=50)),
                ('position', models.CharField(verbose_name='职位', max_length=100)),
                ('department', models.CharField(verbose_name='部门', blank=True, max_length=50)),
                ('worktype', models.CharField(max_length=2, default='FT', choices=[('FT', 'Full-time'), ('IN', 'Intern')])),
                ('acceptnum', models.IntegerField(null=True)),
                ('lowsalary', models.CharField(blank=True, null=True, max_length=20)),
                ('highsalary', models.CharField(blank=True, null=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('experience', models.CharField(blank=True, max_length=20)),
                ('degree', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('latitude', models.DecimalField(blank=True, null=True, decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(blank=True, null=True, decimal_places=7, max_digits=10)),
                ('duty', models.TextField(blank=True, max_length=4000)),
                ('demand', models.TextField(blank=True, max_length=4000)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_activated', models.BooleanField(default=True)),
                ('is_hot', models.BooleanField(default=False)),
                ('refresh', models.DateField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, null=True, max_length=30, default='0')),
                ('top', models.BooleanField(default=False)),
                ('company', models.ForeignKey(to='main.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='语言名', blank=True, null=True, max_length=50)),
                ('proficiency', models.CharField(verbose_name='熟练度', blank=True, null=True, max_length=50, choices=[('M', '母语'), ('F', '流利'), ('G', '一般')])),
                ('subject', models.CharField(verbose_name='科目', blank=True, null=True, max_length=50)),
                ('score', models.CharField(verbose_name='成绩', blank=True, null=True, max_length=50)),
                ('is_activated', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('userid', models.CharField(blank=True, max_length=20)),
                ('usertype', models.CharField(blank=True, max_length=2, choices=[('u', 'user'), ('w', 'wechat_user'), ('c', 'company')])),
                ('url', models.CharField(blank=True, max_length=200)),
                ('ip', models.CharField(blank=True, max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('timestamps', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='logintime',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(null=True, to='main.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('resume', models.FileField(upload_to=main.models.resume_path)),
                ('filename', models.CharField(blank=True, max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_defaulted', models.BooleanField(default=False)),
                ('is_activated', models.BooleanField(default=True)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialWorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('associations', models.CharField(verbose_name='社团名', blank=True, null=True, max_length=50)),
                ('area', models.CharField(verbose_name='地区', blank=True, null=True, max_length=50)),
                ('position', models.CharField(verbose_name='职位', blank=True, max_length=50)),
                ('duties', models.TextField(verbose_name='职责', blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_activated', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='软件名', blank=True, null=True, max_length=50)),
                ('proficiency', models.CharField(verbose_name='熟练度', blank=True, null=True, max_length=50, choices=[('P', '精通'), ('S', '熟练'), ('G', '一般')])),
                ('is_activated', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=100)),
                ('duration', models.IntegerField(choices=[(30, '30 seconds'), (60, '60 seconds'), (90, '90 seconds'), (120, '120 seconds')], default=60)),
                ('job', models.ForeignKey(to='main.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('unique_id', models.CharField(unique=True, max_length=100, default=uuid.uuid4)),
                ('username', models.CharField(blank=True, max_length=50)),
                ('userpwd', models.CharField(blank=True, max_length=80)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('gender', models.CharField(max_length=1, default='M', choices=[('M', 'Male'), ('F', 'Female')])),
                ('wechat_openid', models.CharField(blank=True, max_length=50)),
                ('wechat_informid', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('avatar', models.ImageField(blank=True, upload_to='avatar')),
                ('school', models.CharField(blank=True, max_length=50)),
                ('major', models.CharField(blank=True, max_length=50)),
                ('degree', models.CharField(max_length=1, default='B', choices=[('J', 'Junior college'), ('B', 'Bachelor'), ('M', 'Master'), ('P', 'PhD')])),
                ('gradyear', models.IntegerField(blank=True, null=True)),
                ('is_activated', models.BooleanField(default=False)),
                ('register_date', models.DateTimeField(blank=True, null=True)),
                ('last_login_date', models.DateTimeField(blank=True, null=True)),
                ('is_vip_user', models.BooleanField(default=False)),
                ('review', models.TextField(blank=True, null=True)),
                ('searched', models.TextField(blank=True, null=True)),
                ('birth', models.DateField(verbose_name='出生年月', blank=True, null=True)),
                ('interest', models.TextField(verbose_name='兴趣爱好', blank=True, null=True)),
                ('integrity', models.IntegerField(verbose_name='信息完整度', blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('uber_benefit', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('path', models.FilePathField(path=main.models.video_path)),
                ('application', models.ForeignKey(to='main.Application')),
                ('topic', models.ForeignKey(to='main.Topic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('company', models.CharField(verbose_name='公司名', blank=True, max_length=50)),
                ('position', models.CharField(verbose_name='职位', blank=True, max_length=50)),
                ('department', models.CharField(verbose_name='部门', blank=True, null=True, max_length=50)),
                ('duties', models.TextField(verbose_name='职责', blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_activated', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to='main.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='software',
            name='user',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialworkexperience',
            name='user',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logintime',
            name='user',
            field=models.ForeignKey(null=True, to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='language',
            name='user',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='educationexpericence',
            name='user',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='ccomment',
            field=models.ForeignKey(null=True, to='main.Company'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='ucomment',
            field=models.ForeignKey(null=True, to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='certificate',
            name='user',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(to='main.Job'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.ForeignKey(to='main.Resume'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
    ]
