from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    sex = (
        ('male', '男'),
        ('female', '女')
    )
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default="")
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=sex, default='female', max_length=64)
    address = models.CharField(max_length=128, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    avatar = models.ImageField(upload_to='media/avatar', default='media/avatar/default.png', max_length=255)

    class Meta:
        verbose_name = '用户信息'

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    send_types = (
        ('register', '注册'),
        ('forget', '找回密码')
    )
    code = models.CharField(verbose_name='验证码', max_length=32)
    email = models.EmailField(max_length=64, verbose_name='邮箱')
    send_type = models.CharField(choices=send_types, max_length=32)
    datetime = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'


class Banner(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    banner = models.ImageField(verbose_name='轮播图', upload_to='media/banner', max_length=128)
    url = models.URLField(verbose_name='访问地址', max_length=256)
    index = models.IntegerField(default=1000,verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播图'

    def __str__(self):
        return self.title
