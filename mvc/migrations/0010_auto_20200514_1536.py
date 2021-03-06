# Generated by Django 3.0.5 on 2020-05-14 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0009_auto_20200514_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionticket',
            name='beginTime',
            field=models.DateTimeField(blank=True, verbose_name='开始打印时间'),
        ),
        migrations.AlterField(
            model_name='admissionticket',
            name='endTime',
            field=models.DateTimeField(blank=True, verbose_name='结束打印时间'),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 15, 36, 26, 978349), verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='interviewnotification',
            name='beginTime',
            field=models.DateTimeField(blank=True, verbose_name='开始打印时间'),
        ),
        migrations.AlterField(
            model_name='interviewnotification',
            name='endTime',
            field=models.DateTimeField(blank=True, verbose_name='结束打印时间'),
        ),
    ]
