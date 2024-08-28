from django import template
from ..models import Category, Product

register = template.Library()


@register.simple_tag
def define(val=None):
    return val
