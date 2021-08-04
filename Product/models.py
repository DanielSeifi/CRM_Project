from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name=_('نام محصول'), )
    price = models.PositiveIntegerField(verbose_name=_('قیمت'), )
    is_tax = models.BooleanField(default=False, verbose_name=_('مشمول مالیات'), )
    pdf_file = models.FileField(upload_to='Product/PDFs', verbose_name=_('کاتولوگ محصول'), blank=True,
                                validators=[FileExtensionValidator(['pdf'])], )
    image_file = models.ImageField(upload_to='Product/Images', verbose_name=_('تصویر محصول'), blank=True, )
    feature = models.TextField(verbose_name=_('ویژگی های محصول'), blank=True, )
    company_rel_organ = models.ManyToManyField('Organization.OrganizationProduct',
                                               verbose_name=_('قابل استفاده برای تولید محصولات تولیدی'), )

    class Meta():
        verbose_name = _("محصول")
        verbose_name_plural = _("محصولات")

    def __str__(self):
        return self.product_name

    def get_products_sug(self):
        return [product.name for product in self.company_rel_organ.all()]
