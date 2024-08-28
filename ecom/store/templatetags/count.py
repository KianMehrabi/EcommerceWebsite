from django import template
from ..models import Category, Product

register = template.Library()


"""
    i use custom template tags for counting , checking and ... 
    anything that is not iterable i try to do it here 
    
    here is the my logic steps
    models > custom tags > views
"""


@register.simple_tag
def count_of_all_categories():
    print(type(Category.objects.count()))
    return Category.objects.count()


@register.simple_tag
def count_of_all_products():
    return Product.objects.count()
