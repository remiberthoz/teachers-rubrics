from django.http import HttpResponse

# Create your views here.
from core.models import Exam
from ...htmx_render import htmx_render_page


def display_exam(request, exam_id):
    exams = Exam.objects.all()
    exam = Exam.objects.get(id=exam_id)
    return HttpResponse(htmx_render_page(request, 'ui_htmx/display_exam/main.html', {'exams': exams, 'exam': exam}))
