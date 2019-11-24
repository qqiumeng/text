from django.db import models


# Create your models here.
class ManageUsers(models.Model):
    login_name = models.CharField(max_length=20)  # 登录名
    password = models.CharField(max_length=20)  # 密码
    real_name = models.CharField(max_length=10)  # 真实姓名
    email = models.EmailField()  # 邮箱
    state = models.CharField(max_length=20)  # 状态
    role = models.CharField(max_length=20)  # 角色
    jurisdiction = models.CharField(max_length=100)  # 权限
