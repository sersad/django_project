from django import template

register = template.Library()

# https://pythoncircle.com/post/701/how-to-set-a-variable-in-django-template/


@register.simple_tag
def setvar(val=None):
    return val
