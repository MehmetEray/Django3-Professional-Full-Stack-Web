from django import template
from blog.models import category

register = template.Library()


@register.simple_tag
def kategori_list():
    kategoriler = category.objects.all()
    return kategoriler
