# Generated by Django 3.1.7 on 2021-03-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cand_Reg', '0014_auto_20210324_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availableslotsmodel',
            name='candidate_id',
        ),
        migrations.AlterField(
            model_name='availableslotsmodel',
            name='user_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
