# Generated by Django 3.1.7 on 2021-03-24 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cand_Reg', '0012_remove_availableslotsmodel_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableslotsmodel',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Cand_Reg.usermodel'),
        ),
    ]