from django import template
from core.models import GradedItemInReport

register = template.Library()

@register.filter
def get_item_in_report(report_id, item_id):
    try:
        return GradedItemInReport.objects.get(report_id=report_id, grade_item_id=item_id)
    except GradedItemInReport.DoesNotExist:
        return None
