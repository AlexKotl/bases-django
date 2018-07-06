from django import template

register = template.Library()

@register.filter
def draw_stars(value):
    return "xxxxx"
