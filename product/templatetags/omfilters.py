from django.template import Library
from utils import tools

register = Library()

@register.filter
def reform_price(value):
    return tools.price_format(value)

