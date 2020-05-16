# Generated by Django 2.2.12 on 2020-05-16 21:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0021_auto_20200516_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='atsetinfo',
            name='ifBase',
            field=models.BooleanField(default='0', verbose_name='是否基础模板'),
        ),
        migrations.AddField(
            model_name='insetinfo',
            name='ifBase',
            field=models.BooleanField(default='0', verbose_name='是否基础模板'),
        ),
        migrations.AlterField(
            model_name='atsetinfo',
            name='exam',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
        ),
        migrations.AlterField(
            model_name='examinee',
            name='theExam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 21, 13, 17, 227741), verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='insetinfo',
            name='exam',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
        ),
    ]