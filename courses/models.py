from datetime import datetime

from django.db import models


# Create your models here.
class Course(models.Model):
    degrees = (
        ('cj', '初级'),
        ('zj', '中级'),
        ('gj', '高级')
    )
    name = models.CharField(verbose_name='课程名称', max_length='64')
    desc = models.CharField(verbose_name='课程描述', max_length=256)
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(verbose_name='课程难度', choices=degrees, max_length=8)
    learn_time = models.IntegerField(default=0, verbose_name='学习时长(分钟)')
    stu_count = models.IntegerField(default=0, verbose_name='学习人数')
    fav_counts = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='media/course', default='media/course/default.jpg', verbose_name='课程封面',
                              max_length=128)
    click_count = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程'

class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)