from django import template
from core.models import GradedItemInReport

register = template.Library()

@register.filter
def fromgradeitem(things, gradeitem_id):
    try:
        return things.get(grade_item_id=gradeitem_id)
    except GradedItemInReport.DoesNotExist:
        return None
