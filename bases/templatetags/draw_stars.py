from django import template

register = template.Library()

@register.filter
def draw_stars(rating):
    html = '';

    if rating == 0:
        return ''

    for i in range(1, 6):
        if rating < i:
            if rating >= i - 0.5:
                star = 'half'
            else:
                star = 'off'
        else:
            star = 'on'
        html += "<span class='icon star {star}' alt='' title='{rating}'></span>".format(star=star, rating=round(rating,1))
    return html
