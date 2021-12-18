from django.http import HttpResponse

# Create your views here.
from core.models import GradeItem, Section, Report, Exam, class_save, class_delete, class_get
from ...htmx_render import htmx_render_overlay
from .display import display_exam


def edit_exam(request, exam_id):

    if request.method == 'GET':
        exam = class_get(Exam, exam_id, name='', degree='', year='')
        context = {'exam_id': exam_id, 'exam': exam}
        return HttpResponse(htmx_render_overlay(request, 'ui_htmx/display_exam/modals/report.html', context))

    if request.method == 'POST' and 'student_id' in request.POST:
        class_save(Exam, exam_id, name=request.POST['exam_name'], degree=request.POST['exam_degree'], year=request.POST['exam_year'])
    elif request.method == 'DELETE':
        class_delete(Exam, exam_id)

    return display_exam(request, exam_id)


def edit_section(request, exam_id, section_id):

    if request.method == 'GET':
        section = class_get(Section, section_id, exam_id=exam_id, name='')
        context = {'exam_id': exam_id, 'section': section}
        return HttpResponse(htmx_render_overlay(request, 'ui_htmx/display_exam/modals/section.html', context))

    if request.method == 'POST' and 'section_name' in request.POST:
        class_save(Section, section_id, exam_id=exam_id, name=request.POST['section_name'])
        if 'item_id' in request.POST and 'section_id' in request.POST:
            item_ids = request.POST.getlist('item_id')
            section_ids = request.POST.getlist('section_id')
            for i in range(len(item_ids)):
                item_id = item_ids[i]
                section_id = section_ids[i]

                print(i, item_id)
                item = GradeItem.objects.get(id=item_id)

                item.position_in_section = i
                item.section_id = section_id
                
                item.save()

    elif request.method == 'DELETE':
        class_delete(Section, section_id)

    return display_exam(request, exam_id)


def edit_report(request, exam_id, report_id):

    if request.method == 'GET':
        report = class_get(Report, report_id, exam_id=exam_id, student_id='')
        context = {'exam_id': exam_id, 'report': report}
        return HttpResponse(htmx_render_overlay(request, 'ui_htmx/display_exam/modals/report.html', context))

    if request.method == 'POST' and 'student_id' in request.POST:
        class_save(Report, report_id, exam_id=exam_id, student_id=request.POST['student_id'])
    elif request.method == 'DELETE':
        class_delete(Report, report_id)

    return display_exam(request, exam_id)


def edit_item(request, exam_id, section_id, item_id):

    if request.method == 'GET':
        item = class_get(GradeItem, item_id, section_id=section_id, desc='', position_in_section=0)
        context = {'exam_id': exam_id, 'item': item}
        return HttpResponse(htmx_render_overlay(request, 'ui_htmx/display_exam/modals/item.html', context))

    if request.method == 'POST' and 'section_id' in request.POST and 'desc' in request.POST:
        class_save(GradeItem, item_id, section_id=section_id, desc=request.POST['desc'], position_in_section=0)
    elif request.method == 'DELETE':
        class_delete(GradeItem, item_id)

    return display_exam(request, exam_id)
