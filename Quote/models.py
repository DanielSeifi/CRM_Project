from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum, F, Case, When
from django_jalali.db import models as jdate
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from Organization.models import Organization
from Product.models import Product


class Quote(models.Model):
    user_creator = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name=_('کاربر ثبت کننده'))
    organ = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name=_('سازمان'))
    created_at = jdate.jDateTimeField(auto_now_add=True, verbose_name=_('تاریخ ثبت'))
    tax = 9

    class Meta:
        verbose_name = _('پیش فاکتور')
        verbose_name_plural = _('پیش فاکتور ها')

    def __str__(self):
        return f'{self.organ}'

    def get_total_quantity(self):
        return self.quoteitem_set.all().aggregate(Sum('quantity')).get('quantity__sum', 0)

    def get_total_base_price(self):
        return self.quoteitem_set.all().annotate(total_base_price=F('quantity') * F('price')) \
            .aggregate(Sum('total_base_price'))['total_base_price__sum']

    def get_quote_discount(self):
        return self.quoteitem_set.all().annotate(
            total_base_price=F('quantity') * F('price')).annotate(
            total_discount=(F('discount') * F('total_base_price') / 100)) \
            .aggregate(Sum('total_discount'))['total_discount__sum']

    def get_quote_tax(self, tax=tax):
        return self.quoteitem_set.all().annotate(
            total_base_price=F('quantity') * F('price')).annotate(
            total_price=F('total_base_price') - (F('discount') * F('total_base_price') / 100)).annotate(
            total_tax=Case(
                When(product__is_tax=True, then=(F('total_price') * tax / 100)),
                When(product__is_tax=False, then=0),
                output_field=models.PositiveIntegerField()
            )
        ).aggregate(Sum('total_tax'))['total_tax__sum']

    def get_total_price(self, tax=tax):
        return self.quoteitem_set.all().annotate(
            total_base_price=F('quantity') * F('price')).annotate(
            total_price=F('total_base_price') - (F('discount') * F('total_base_price') / 100)).annotate(
            total_price=Case(
                When(product__is_tax=True, then=F('total_price') + (F('total_price') * tax / 100)),
                When(product__is_tax=False, then=F('total_price')),
                output_field=models.PositiveIntegerField()
            )
        ).aggregate(Sum('total_price'))['total_price__sum']



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
