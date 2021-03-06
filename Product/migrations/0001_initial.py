# Generated by Django 3.2.5 on 2021-07-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام محصول')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت')),
                ('is_tax', models.BooleanField(default=False, verbose_name='مشمول مالیات')),
                ('pdf_file', models.FileField(blank=True, upload_to='Product/PDFs', verbose_name='کاتولوگ محصول')),
                ('image_file', models.ImageField(blank=True, upload_to='Product/Images', verbose_name='تصویر محصول')),
                ('feature', models.TextField(blank=True, verbose_name='ویژگی های محصول')),
                ('company_rel_organ', models.ManyToManyField(to='Organization.OrganizationProduct', verbose_name='قابل استفاده برای تولید محصولات تولیدی')),
            ],
        ),
    ]
