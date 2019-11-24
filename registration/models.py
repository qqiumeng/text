from django.db import models

# Create your models here.
# 医生表



class Departments(models.Model):
    department_name = models.CharField(max_length=10)


# Create your models here.
# 病号表
# class Patient(models.Model):
#     name = models.CharField(max_length=10)  # 姓名
#     certificate_type = models.CharField(max_length=10,default='身份证')  # 证件类型
#     id_num = models.IntegerField()