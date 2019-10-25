from django.db import models
from .studentmodel import StudentBasic

class StudentExamExtra(models.Model):
    class Meta:
        verbose_name = '心理学员补考情况'
        verbose_name_plural = verbose_name

    relate_student = models.OneToOneField(StudentBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    # relate_student = models.ForeignKey(StudentBasic, on_delete=models.DO_NOTHING, verbose_name='学号')
    exam_date = models.CharField(max_length=128,verbose_name='报考日期', null=True, blank=True)
    exam_theory = models.CharField(max_length=128, verbose_name='理论报考', blank=True, null=True)
    exam_theory_result = models.CharField(max_length=128, verbose_name='理论成绩', blank=True, null=True)
    exam_practise = models.CharField(max_length=128, verbose_name='实操报考', blank=True, null=True)
    exam_practise_result = models.CharField(max_length=128, verbose_name='实操成绩', blank=True, null=True)
    exam_total = models.CharField(max_length=128, verbose_name='综合报考', blank=True, null=True)
    exam_total_result = models.CharField(max_length=128, verbose_name='综合成绩', blank=True, null=True)
    exam_status = models.CharField(max_length=128, verbose_name='合格情况', blank=True, null=True)

    def get_stu_name(self):
        return self.relate_student.stu_name

    get_stu_name.short_description = u'姓名'
    get_stu_name.allow_tags = get_stu_name.is_column = True

    def get_stu_num(self):
        return self.relate_student.stu_number

    get_stu_num.short_description = '学号'
    get_stu_num.allow_tags = get_stu_num.is_colume = True

    def get_stu_class(self):
        return self.relate_student.stu_class.class_name

    get_stu_class.short_description = u'班级'
    get_stu_class.allow_tags = get_stu_name.is_column = True

    def __str__(self):
        return str(self.get_stu_name())


