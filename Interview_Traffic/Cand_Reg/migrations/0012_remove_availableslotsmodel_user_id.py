# Generated by Django 3.1.7 on 2021-03-24 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cand_Reg', '0011_availableslotsmodel_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availableslotsmodel',
            name='user_id',
        ),
    ]