from django.contrib import admin

from .models import Exam, GradeItem, GradedItemInReport, Report, Section

admin.site.register(Exam)
admin.site.register(Section)
admin.site.register(GradeItem)
admin.site.register(Report)
admin.site.register(GradedItemInReport)
