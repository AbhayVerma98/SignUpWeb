# Generated by Django 3.1.5 on 2021-10-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')], max_length=20, null=True),
        ),
    ]
