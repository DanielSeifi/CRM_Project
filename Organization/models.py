from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jdate

phone_regex = RegexValidator(
    regex='^(\+98|0)?\d{1,2}\d{1,8}$',
    message=_("تلفن وارد شده معتبر نیست"),
    code='invalid_phone',
)


# Create your models here.

class OrganizationProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("محصولات تولیدی"), )

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("استان"), unique=True, )

    def __str__(self):
        return self.name


class Organization(models.Model):
    state = models.ForeignKey(State, verbose_name=_("استان"), on_delete=models.PROTECT, default=None, )
    name = models.CharField(max_length=200, verbose_name=_("نام سازمان"), unique=True, )
    phone = models.CharField(max_length=11, verbose_name=_("تلفن"), validators=[phone_regex], )
    workers_qty = models.PositiveIntegerField(default=1, verbose_name=_("تعداد کارگران"), )
    organ_product = models.ManyToManyField('OrganizationProduct', verbose_name=_("محصولات تولیدی"), )
    full_name_owner = models.CharField(max_length=200, verbose_name=_("نام و نام خانوادگی مخاطب"), default=None, )
    phone_owner = models.CharField(max_length=11, verbose_name=_("تلفن مخاطب"), validators=[phone_regex], )
    email_owner = models.EmailField(verbose_name=_("ایمیل مخاطب"), blank=True, )
    created_at = jdate.jDateTimeField(verbose_name=_("تاریخ ثبت"), auto_now_add=True, )
    user_creator = models.ForeignKey(get_user_model(), verbose_name=_("کاربر ایجاد کننده"), on_delete=models.PROTECT)

    def __str__(self):
        return self.name
