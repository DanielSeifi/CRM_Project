# Generated by Django 3.2.5 on 2021-07-29 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_rename_name_product_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
