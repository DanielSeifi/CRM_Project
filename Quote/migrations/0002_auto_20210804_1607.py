# Generated by Django 3.2.5 on 2021-08-04 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='organization',
            new_name='organ',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='creator',
            new_name='user_creator',
        ),
    ]