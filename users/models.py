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
