from django.db import models
from hospital.models import *
from django.core import validators

# Create your models here.


class Drug(models.Model):
    drug_num = models.CharField(max_length=20)  # 药品编号
    drug_img = models.FileField(upload_to='picture')  # 药品图片
    purchasing_price = models.FloatField()  # 进价
    selling_price = models.FloatField()  # 售价
    drug_name = models.CharField(max_length=20)  # 药品名称
    drug_type = models.CharField(max_length=20)  # 药品类型
    brief_description = models.CharField(max_length=20)  # 简单描述
    expiration_time = models.CharField(max_length=50)  # 过期时间
    detail = models.TextField()  # 详细描述
    manufacturer = models.CharField(max_length=20)  # 生产厂商
    taking_instructions = models.TextField()  # 服用说明
    inventory = models.IntegerField(default=3000)  # 库存
    surplus = models.IntegerField(default=0)  # 剩余量
    remark = models.CharField(max_length=20)  # 备注
    state = models.CharField(max_length=20, default='未销售')  # 药品的销售状态


class Drug_grant(models.Model):
    drup_num = models.IntegerField()  # 药品总数量
    sent = models.IntegerField(default=0)  # 已发放数量
    not_sent = models.IntegerField()  # 未发放数量
    principal = models.CharField(max_length=10)  # 负责人
    case_id = models.ForeignKey(Patient, on_delete=models.CASCADE)  # 与病号表外键关联显示病历号，姓名
    drug_name_id = models.ForeignKey(Drug, on_delete=models.CASCADE)  # 与药品表外键关联显示药品名称

