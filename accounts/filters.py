from django.core.files.base import endswith_cr
from django.db.models import fields
from django.db.models.base import Model
import django_filters
from django_filters.filters import CharFilter, DateFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']