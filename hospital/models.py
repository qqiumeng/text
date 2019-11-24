from django.db import models
from doctor.models import Doctor


# Create your models here.

# 病号表
class Patient(models.Model):
    name = models.CharField(max_length=10)  # 姓名
    certificate_type = models.CharField(max_length=10, default='身份证')  # 证件类型
    id_num = models.CharField(max_length=20)  # 证件号
    social_security_num = models.CharField(max_length=20)  # 社保号
    tel = models.CharField(max_length=20)  # 联系电话
    self_pay = models.CharField(default='否', max_length=10)  # 是否自费
    sex = models.CharField(max_length=5)  # 性别
    age = models.IntegerField()  # 年龄
    occupation = models.CharField(max_length=10)  # 职业
    visit = models.CharField(max_length=5)  # 初复诊
    money = models.FloatField(default=2000)  # 押金金额
    remark = models.CharField(max_length=100)  # 备注
    # medical_record_No = models.IntegerField()  # 病历号
    g_time = models.DateField(auto_now_add=True)  # 挂号时间
    state = models.CharField(max_length=10, default='已挂号')  # 状态
    g_money = models.FloatField(default=10)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # 与医生表外键关联显示指定医生和所挂科室

    def __str__(self):
        return self.name

# 收费项目表
class Charge_manage(models.Model):
    charge_cellectable = models.CharField(max_length=20)  # 收费项目
    charge_amount = models.FloatField()  # 收费金额
    exam_date = models.DateTimeField(auto_now_add=True)  # 检查日期
    all_charge = models.FloatField()  # 总收费

    def __str__(self):
        return self.charge_cellectable

#检查收费项目表
class Charge(models.Model):
    charge_manage_id = models.ForeignKey(Charge_manage, on_delete=models.CASCADE)  # 与收费项目表外键关联显示病历收费项目，收费金额，检查日期，总收费
    case_id = models.ForeignKey(Patient, on_delete=models.CASCADE)  # 与病号表外键关联显示病历号，姓名，日期


# 住院表
class Hospital(models.Model):
    bed_num = models.IntegerField(null=True)  # 床号
    cash = models.FloatField()  # 押金
    into_data = models.DateField(auto_now_add=True)  # 入院时间
    state = models.CharField(max_length=20)  # 状态
    nurse = models.CharField(max_length=30)  # 护理人员
    illness = models.TextField()  # 病情
    case_id = models.ForeignKey(Patient, on_delete=models.CASCADE)  # 与病号表外键关联显示病历号和当前余额，病人姓名，联系电话
    office_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # 与医生表关联显示科室及指定医生
    object_id = models.ForeignKey(Charge, on_delete=models.CASCADE, null=True)  # 与收费表关联显示收费项目，收费金额，收费日期

    def __str__(self):
        return self.case_id.name
