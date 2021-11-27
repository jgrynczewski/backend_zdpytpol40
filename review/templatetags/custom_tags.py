from django import template

register = template.Library()

def trim(value):
    if len(value) > 5:
        return value[:5]
    return value


register.filter('trim', trim)
