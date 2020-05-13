# Generated by Django 3.0.5 on 2020-05-11 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionticket',
            name='theExam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam'),
        ),
        migrations.AlterField(
            model_name='admissionticket',
            name='theExaminee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mvc.Examinee'),
        ),
        migrations.AlterField(
            model_name='interviewnotification',
            name='theExam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.Exam'),
        ),
        migrations.AlterField(
            model_name='interviewnotification',
            name='theExaminee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mvc.Examinee'),
        ),
    ]