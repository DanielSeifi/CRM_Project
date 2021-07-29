# Generated by Django 3.2.5 on 2021-07-29 10:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='محصولات تولیدی')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='استان')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='نام سازمان')),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='تلفن وارد شده معتبر نیست', regex='^(\\+98|0)?\\d{1,2}\\d{1,8}$')], verbose_name='تلفن')),
                ('workers_qty', models.PositiveIntegerField(default=1, verbose_name='تعداد کارگران')),
                ('full_name_owner', models.CharField(default=None, max_length=200, verbose_name='نام و نام خانوادگی مخاطب')),
                ('phone_owner', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='تلفن وارد شده معتبر نیست', regex='^(\\+98|0)?\\d{1,2}\\d{1,8}$')], verbose_name='تلفن مخاطب')),
                ('email_owner', models.EmailField(blank=True, max_length=254, verbose_name='ایمیل مخاطب')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('organ_product', models.ManyToManyField(to='Organization.OrganizationProduct', verbose_name='محصولات تولیدی')),
                ('state', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='Organization.state', verbose_name='استان')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر ایجاد کننده')),
            ],
        ),
    ]