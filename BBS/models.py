from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Category(models.Model):  # 板块
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey('BBS_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BBS(models.Model):  # 文章
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user', on_delete=models.CASCADE)  # 级联删除
    view_count = models.IntegerField(default=0)
    ranking = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bbs:bbs_detail', kwargs={'bbs_id': self.id})


class BBS_user(models.Model):  # 用户
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signature = models.CharField(max_length=28, default='Nothing')
    # upload_to 会自动在项目的根目录下创建upload_img文件夹，带年纪
    photo = models.ImageField(upload_to='upload_imgs', default='upload_imgs/user1.jpg')

    def __str__(self):
        return self.user.username
