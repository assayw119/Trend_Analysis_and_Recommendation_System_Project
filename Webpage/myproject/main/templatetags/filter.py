from django import template

register = template.Library()

@register.filter(name='split')
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep)[0]