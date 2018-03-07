from django import template
import re

register = template.Library()

@register.filter
def highlighter(value, search):
    redata = re.compile(re.escape(search), re.IGNORECASE)
    newval = redata.sub("<span class=\"highlight\">{}</span>".format(search), value)
    return newval

