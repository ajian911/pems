# Generated by Django 3.0.5 on 2020-05-14 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0008_auto_20200514_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionticket',
            name='date',
            field=models.DateField(blank=True, verbose_name='考试日期'),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 14, 40, 37, 108417), verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='interviewnotification',
            name='date',
            field=models.DateField(blank=True, verbose_name='考试日期'),
        ),
    ]
