from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def make_rating_icon(score):

    if score == '':
        score = -1
    score = int(score)

    if score == 0:
        return mark_safe("""<div class="ui blue rating disabled"><i class="small circle icon"></i></div>""")
    if score == 1:
        return mark_safe("""<div class="ui blue rating disabled"><i class="star icon"></i></div>""")
    if score == 2:
        return mark_safe("""<div class="ui blue rating disabled"><i class="star icon active"></i></div>""")
    else:
        return mark_safe(""" """)
        
