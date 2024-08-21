from django import template
from ..models import Product

register = template.Library()

@register.simple_tag
def count_of_all_products():
    return Product.objects.count()