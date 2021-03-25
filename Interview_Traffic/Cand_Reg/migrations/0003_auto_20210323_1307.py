# Generated by Django 3.1.7 on 2021-03-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cand_Reg', '0002_auto_20210322_0743'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Interviewer',
        ),
        migrations.AddField(
            model_name='candidate',
            name='Registration_type',
            field=models.CharField(choices=[('IN', 'Interviewer'), ('CA', 'Candidate')], default='IN', max_length=2),
        ),
    ]
