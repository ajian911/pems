# Generated by Django 3.0.5 on 2020-05-15 10:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0013_auto_20200514_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATSetInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('beginTime', models.DateTimeField(null=True, verbose_name='开始打印时间')),
                ('endTime', models.DateTimeField(null=True, verbose_name='结束打印时间')),
                ('state', models.BooleanField(default='0', verbose_name='当前状态')),
            ],
        ),
        migrations.CreateModel(
            name='INSetInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('checkInTime', models.TimeField(blank=True, null=True, verbose_name='报到时间')),
                ('drawTime', models.TimeField(blank=True, null=True, verbose_name='抽签时间')),
                ('deadlineTime', models.TimeField(blank=True, null=True, verbose_name='截止时间')),
                ('stratIVTime', models.TimeField(blank=True, null=True, verbose_name='开始时间')),
                ('beginTime', models.DateTimeField(blank=True, null=True, verbose_name='开始打印时间')),
                ('endTime', models.DateTimeField(blank=True, null=True, verbose_name='结束打印时间')),
                ('state', models.BooleanField(default='0', verbose_name='当前状态')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='用户名')),
                ('realName', models.CharField(max_length=50, verbose_name='真实姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
            ],
        ),
        migrations.DeleteModel(
            name='admissionTicket',
        ),
        migrations.DeleteModel(
            name='interviewNotification',
        ),
        migrations.RenameField(
            model_name='examinee',
            old_name='IDNumber',
            new_name='IDNO',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='adress',
        ),
        migrations.AddField(
            model_name='exam',
            name='siteAddress',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='考点地址'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subjectName',
            field=models.CharField(default=111, max_length=100, verbose_name='考试科目'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='subjectTime',
            field=models.CharField(default=111, max_length=100, verbose_name='科目时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examinee',
            name='applyPosition',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='报考职位'),
        ),
        migrations.AddField(
            model_name='examinee',
            name='applyUnit',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='报考单位'),
        ),
        migrations.AddField(
            model_name='examinee',
            name='ifPrint',
            field=models.BooleanField(default='0', verbose_name='是否已打印'),
        ),
        migrations.AddField(
            model_name='examinee',
            name='ifQuery',
            field=models.BooleanField(default='0', verbose_name='是否已查询'),
        ),
        migrations.AddField(
            model_name='examinee',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码'),
        ),
        migrations.AddField(
            model_name='examinee',
            name='theExam',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exam',
            name='examMethod',
            field=models.CharField(choices=[('面试', '面试'), ('笔试', '笔试'), ('机考', '机考'), ('其他', '其他')], default=('笔试', '笔试'), max_length=20, verbose_name='考试形式'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='examineeNum',
            field=models.IntegerField(blank=True, null=True, verbose_name='考生人数'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='remarks',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='siteName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='考点名称'),
        ),
        migrations.AlterField(
            model_name='examinee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 10, 2, 42, 805266), verbose_name='上传时间'),
        ),
        migrations.AddField(
            model_name='insetinfo',
            name='exam',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
        ),
        migrations.AddField(
            model_name='atsetinfo',
            name='exam',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam', verbose_name='关联考试'),
        ),
        migrations.AddField(
            model_name='examinee',
            name='ATInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mvc.ATSetInfo', verbose_name='关联准考证'),
        ),
        migrations.AddField(
            model_name='examinee',
            name='INInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mvc.INSetInfo', verbose_name='关联通知书'),
        ),
    ]
