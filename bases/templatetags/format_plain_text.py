from django import template
import re

register = template.Library()

@register.filter
def format_plain_text(text):
    text = re.sub("\n", "<br>", text)
    text = re.sub("[[:alpha:]]+://[^<>[:space:]]+[[:alnum:]/]", "<a href='away.php?url=\\0' target='_blank'>\\0</a>", text)
    text = re.sub("(^| |\n)(www([.]?[a-zA-Z0-9_/-])*)", "\\1<a href=\"/away.php?url=http://\\2\" target='_blank'>\\2</a>", text)

    return text
