from django.urls import path

from . import views
from .subviews.reports import edits as reports_edits
from .subviews.exams import edits as exams_edits, display as exams_displays

urlpatterns = [
    path('<int:exam_id>/report-<int:report_id>/grade-item-<int:item_id>/', reports_edits.grade_item, name='grade-item'),
    path('<int:exam_id>/edit-section-<int:section_id>/', exams_edits.edit_section, name='edit-section'),
    path('<int:exam_id>/edit-section-<int:section_id>-item-<int:item_id>/', exams_edits.edit_item, name='edit-item'),
    path('<int:exam_id>/edit-report-<int:report_id>/', exams_edits.edit_report, name='edit-report'),
    path('<int:exam_id>/', exams_displays.display_exam, name='display-exam'),
    path('', views.index, name='index'),
]
