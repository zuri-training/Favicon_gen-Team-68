from django import template

register = template.Library()

def split(value, arg):
    return value.split(arg)[-1]

register.filter('split', split)
