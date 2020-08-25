from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
import datetime
from product.models import Product

from decimal import Decimal
CURRENCY = settings.CURRENCY


class OrderManager(models.Manager):

    def active(self):
        return self.filter(active=True)


class Order(models.Model):
    date = models.DateField(default=datetime.datetime.now())
    title = models.CharField(blank=True, max_length=150)
    timestamp = models.DateField(auto_now_add=True)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=True)
    objects = models.Manager()
    browser = OrderManager()

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        order_items = self.order_items.all()
        self.value = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        self.final_value = Decimal(self.value) - Decimal(self.discount)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'New Order'

    def get_edit_url(self):
        return reverse('update_order', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('delete_order', kwargs={'pk': self.id})

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'

    def tag_discount(self):
        return f'{self.discount} {CURRENCY}'

    def tag_value(self):
        return f'{self.value} {CURRENCY}'

    @staticmethod
    def filter_data(request, queryset):
        search_name = request.GET.get('search_name', None)
        date_start = request.GET.get('date_start', None)
        date_end = request.GET.get('date_end', None)
        queryset = queryset.filter(title__contains=search_name) if search_name else queryset
        if date_end and date_start and date_end >= date_start:
            date_start = datetime.datetime.strptime(date_start, '%m/%d/%Y').strftime('%Y-%m-%d')
            date_end = datetime.datetime.strptime(date_end, '%m/%d/%Y').strftime('%Y-%m-%d')
            print(date_start, date_end)
            queryset = queryset.filter(date__range=[date_start, date_end])
        return queryset