# Generated by Django 3.2.5 on 2021-08-04 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name': 'سازمان', 'verbose_name_plural': 'سازمان ها'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'استان', 'verbose_name_plural': 'استان ها'},
        ),
        migrations.AlterUniqueTogether(
            name='organization',
            unique_together={('name', 'user_creator')},
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='گزارش کار')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Organization.organization', verbose_name='نام سازمان')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر ایجاد کننده')),
            ],
            options={
                'verbose_name': 'پیگیری',
                'verbose_name_plural': 'پیگیری ها',
                'unique_together': {('organization',)},
            },
        ),
    ]
