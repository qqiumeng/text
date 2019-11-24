from django.db import models


# Create your models here.
# 资源管理表
class Resource(models.Model):
    r_name = models.CharField(max_length=15,null=False)  # 资源名称
    url = models.CharField(max_length=50,null=False)  # 路径url
    result = models.CharField(max_length=2,default='有效')  # 是否有效
