# Generated by Django 3.2.5 on 2021-08-04 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0002_auto_20210804_0600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationproduct',
            options={'verbose_name': 'محصول تولیدی', 'verbose_name_plural': 'محصولات تولیدی'},
        ),
    ]