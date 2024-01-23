from django import template

from rates import utils

register = template.Library()


@register.simple_tag()
def get_lines():
    rates_data = utils.get_rates_data()
    return rates_data[-10:]
