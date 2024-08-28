from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag("tags/category.html")
def all_categories():
    model = Category.objects.all()
    return {"categories": model}
