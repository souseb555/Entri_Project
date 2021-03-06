# Generated by Django 3.1.7 on 2021-03-24 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cand_Reg', '0005_auto_20210324_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availableslotsmodel',
            name='available_end_date',
        ),
        migrations.RemoveField(
            model_name='availableslotsmodel',
            name='available_start_date',
        ),
        migrations.RemoveField(
            model_name='availableslotsmodel',
            name='user_id',
        ),
        migrations.AddField(
            model_name='availableslotsmodel',
            name='candidate_id',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
        migrations.AddField(
            model_name='availableslotsmodel',
            name='interviewer_id',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='available_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='available_start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
