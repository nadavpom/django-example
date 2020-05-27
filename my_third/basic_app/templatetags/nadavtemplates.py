from django import template

register = template.Library()

@register.filter(name='nadav')
def cut (value, arg):
    return value.replace(arg,'')

# register.filter('cut', cut)
