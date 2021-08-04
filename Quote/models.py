from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_jalali.db import models as jdate
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from Organization.models import Organization
from Product.models import Product


class Quote(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name=_('کاربر ثبت کننده'))
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name=_('سازمان'))
    created_at = jdate.jDateTimeField(auto_now_add=True, verbose_name=_('تاریخ ثبت'))
    tax = 9

    class Meta:
        verbose_name = _('پیش فاکتور')
        verbose_name_plural = _('پیش فاکتور ها')

    def __str__(self):
        return f'{self.organization}'

class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name=_('پیش فاکتور'))
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_('محصول'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('قیمت'))
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name=_('تعداد'))
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], verbose_name=_('درصد تخفیف'))

    class Meta:
        verbose_name = _('رکورد پیش فاکتور')
        verbose_name_plural = _('رکورد پیش فاکتورها')

    def __str__(self):
        return f'{self.quote} {self.product}'

    def get_total_price(self):
        return self.quantity * self.price
