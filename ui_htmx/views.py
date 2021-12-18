from django.http import HttpResponse

from core.models import Exam
from .htmx_render import htmx_render_page


def index(request):
    exams = Exam.objects.order_by("name")
    return HttpResponse(htmx_render_page(request, 'ui_htmx/index.html', {'exams': exams}))
