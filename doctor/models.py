from django.db import models
from registration.models import Departments

# 医生表
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=10)  # 医生姓名（指定医生）
    card_type = models.CharField(max_length=15, default='身份证')  # 证件类型
    card_num = models.CharField(max_length=20)  # 证件号
    phone = models.IntegerField()  # 手机号
    tel = models.IntegerField()  # 座机
    sex = models.CharField(max_length=2)  # 性别
    age = models.IntegerField()  # 年龄
    birth = models.DateTimeField(auto_now_add=True)  # 出生年月日
    email = models.EmailField()  # 电子邮箱
    level = models.CharField(max_length=20)  # 学历
    remark = models.CharField(max_length=50)  # 备注
    in_data = models.DateTimeField(auto_now_add=True)  # 入院日期
    d_number = models.IntegerField()  # 医生编号
    d_office = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.doctor_name