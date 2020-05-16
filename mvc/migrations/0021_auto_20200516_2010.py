# Generated by Django 2.2.12 on 2020-05-16 20:10

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0020_auto_20200515_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atsetinfo',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='模板内容'),
        ),
        migrations.AlterField(
            model_name='atsetinfo',
            name='exam',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
        ),
        migrations.AlterField(
            model_name='examinee',
            name='theExam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 20, 10, 57, 940761), verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='insetinfo',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='模板内容'),
        ),
        migrations.AlterField(
            model_name='insetinfo',
            name='exam',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
        ),
    ]