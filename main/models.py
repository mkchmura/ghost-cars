from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='none')
    slug = models.SlugField(max_length=255, default='none')
    marque = models.CharField(max_length=255, default='none')
    paylink = models.CharField(max_length=255, default='none')
    mintime = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    future = models.BooleanField(default=False)
    bookable = models.BooleanField(default=False)
    price24 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price7 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price24abo = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price7abo = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    franchise = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    franchiseabo = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    kmsupp = models.CharField(max_length=255, default='none')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    principal = models.BooleanField(default=False)
    objects = models.Manager()
    products = ProductManager()


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(f"{self.id}-{self.title}")
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="static/img/",
        default="static/img/token.png",
    )

    alt_text = models.CharField(
        verbose_name=_("Alternativee text"),
        help_text=_("Write an Alt"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

