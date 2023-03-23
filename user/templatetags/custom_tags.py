from django import template
from user.models import *

register = template.Library()

@register.simple_tag
def get_category_name(id):
    return Catagory.objects.get(id=id).name