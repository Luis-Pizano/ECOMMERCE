# Generated by Django 5.0.6 on 2024-09-14 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_name',
            new_name='username',
        ),
    ]
