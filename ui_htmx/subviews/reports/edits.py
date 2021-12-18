from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from core.models import GradedItemInReport
from ui_htmx.templatetags.make_rating_icon import make_rating_icon
from ..exams.display import display_exam


def grade_item(request, exam_id, report_id, item_id):

    try:
        item = GradedItemInReport.objects.get(report_id=report_id, grade_item_id=item_id)
    except ObjectDoesNotExist:
        item = GradedItemInReport(report_id=report_id, grade_item_id=item_id, score=0)

    if request.method == 'DELETE':
        item.delete()
        return display_exam(request, exam_id)

    if request.method == 'POST':
        score = request.POST['score']
        if score == 'cycle':
            if item.score ==  -1: score = 0
            elif item.score == 0: score = 1
            elif item.score == 1: score = 2
            elif item.score == 2: score = -1
            else: score = -1.0
        item.score = score
        item.save()

    return HttpResponse(make_rating_icon(item.score))