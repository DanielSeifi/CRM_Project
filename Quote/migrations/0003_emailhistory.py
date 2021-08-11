# Generated by Django 3.2.5 on 2021-08-11 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quote', '0002_auto_20210804_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='متن ایمیل')),
                ('status', models.BooleanField(verbose_name='وضعیت ارسال')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='ایمیل مخاطب')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quote.quote', verbose_name='پیش فاکتور')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر ثبت کننده')),
            ],
            options={
                'verbose_name': 'تاریخچه ایمیل',
                'verbose_name_plural': 'تاریخچه ایمیل ها',
            },
        ),
    ]
