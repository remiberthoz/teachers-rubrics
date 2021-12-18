from django.db import models
from django.utils.translation import gettext_lazy as _


def class_get(cls, object_id, **kwargs):
    if object_id is not None and object_id != 0:
        return cls.objects.get(id=object_id)
    else:
        return cls(id=0, **kwargs)

def class_save(cls, object_id, **kwargs):
    if object_id is not None and object_id != 0:
        cls.objects.filter(id=object_id).update(**kwargs)
    else:
        cls.objects.create(**kwargs)

def class_delete(cls, object_id):
    cls.objects.get(id=object_id).delete()


#####################################################################
# Exam and components ###############################################

class Exam(models.Model):
    class Meta:
        ordering = ['year', 'degree', 'name']
    name = models.CharField(max_length=1024)
    degree = models.CharField(max_length=1024)
    year = models.IntegerField()


class Section(models.Model):
    class Meta:
        ordering = ['id']
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)


class GradeItem(models.Model):
    class Meta:
        ordering = ['position_in_section', 'id']
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1024)
    position_in_section = models.IntegerField()


#####################################################################
# Actual grades and reports #########################################

class Report(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=1024)


class GradedItemInReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    grade_item = models.ForeignKey(GradeItem, on_delete=models.CASCADE)
    class Score(models.IntegerChoices):
        GOOD = 2, 'Complete, coherent, commented'
        HALF = 1, 'Incomplete, incoherent'
        NOPE = 0, 'Missing important parts, wrong'
        EMPTY = -1, '(Unknown)'
    score = models.IntegerField(choices=Score.choices)
