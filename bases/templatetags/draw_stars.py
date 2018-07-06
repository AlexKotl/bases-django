from django import template

register = template.Library()

def draw_stars(value):
    return "xxxxx"

register.filter('draw_stars', draw_stars)
