from django.shortcuts import render,HttpResponse,redirect
from doctor.models import *
from django import views
from django.core.paginator import Paginator  # 导入分页器
from registration.models import Departments
import datetime, openpyxl
from django.http import JsonResponse

# Create your views here.

# 首页
class index(views.View):
    def get(self,request):
        i = Doctor.objects.all()  # 获取所有医生的数据
        limit = 2
        paginator = Paginator(i,limit)   # 按每页2条分页
        page = request.GET.get("page","1")   # 默认跳转到第一页
        result = paginator.page(page)
        return render(request, 'doctor/index.html',{"i":result})

    def post(self,request):
        """
        信息查询
        :param request:
        :return:
        """

        d_number = request.POST.get("d_number")
        doctor_name = request.POST.get("doctor_name")
        office = request.POST.get("office")
        if len(d_number) >0 and len(doctor_name) > 0 and len(office) > 0:
            d = Doctor.objects.filter(d_number=d_number,doctor_name=doctor_name,office=office)
            return render(request, "doctor/index.html",{'d':d})

        elif len(d_number) > 0:
            d = Doctor.objects.filter(d_number=d_number)
            return render(request, "doctor/index.html",{'d':d})

        elif len(doctor_name) > 0:
            d = Doctor.objects.filter(doctor_name=doctor_name)
            return render(request, "doctor/index.html",{"d": d})

        elif len("office") > 0:
            d_id = Departments.objects.get(department_name=office).id
            d = Doctor.objects.filter(d_office_id=d_id)
            return render(request, "doctor/index.html",{'d':d})

        else:
            return redirect("doctor:index")

# 导出Excel
def dpro(request):
    id_list = []
    ids = request.POST.get('ss')
    wb = openpyxl.Workbook()
    ws = wb.active
    for i in ids:
        if i != ',':
            id_list.append(i)
        else:
            pass
    for i in id_list:
        hos = Doctor.objects.filter(id=int(i))
        ws['A1'].value = '医生编号'
        ws['B1'].value = '医生姓名'
        ws['C1'].value = '入院日期'
        ws['D1'].value = '所属科室'
        row = 2
        for obj in hos:
            ws['A' + str(row)].value = obj.d_number
            ws['B' + str(row)].value = obj.doctor_name
            ws['C' + str(row)].value = obj.in_data
            ws['D' + str(row)].value = obj.d_office.department_name
            row += 1
            wb.save(f'{obj.doctor_name}.xlsx')
            f = open(f'{obj.doctor_name}.xlsx', 'rb')
            p = HttpResponse()
            p.content = f
            p['Content-Type'] = 'application/octet-stream'
            p['Content-Disposition'] = 'attachment;filename="%s.xlsx"' % obj.doctor_name
    return render(request,'doctor/index.html')


# 添加医生
class add(views.View):
    def get(self,request):
        d_all = Departments.objects.all()
        return render(request, 'doctor/add.html', {"d_all": d_all})

    def post(self,request):
        doctor_name = request.POST.get("doctor_name")
        card_type = request.POST.get("card_type")
        card_num = request.POST.get("card_num")
        phone = request.POST.get("phone")
        tel = request.POST.get("tel")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        birth = request.POST.get("birth")
        email = request.POST.get("email")
        office = request.POST.get("office")
        level = request.POST.get("level")
        remark = request.POST.get("remark")
        in_data = request.POST.get("in_data")
        d_number = request.POST.get("d_number")
        d_id = Departments.objects.get(department_name=office).id
        print(doctor_name, card_type, card_num, phone, tel, sex, age, birth, email, office, level, remark, in_data, d_number, d_id)
        Doctor.objects.create(doctor_name=doctor_name, card_type=card_type, card_num=card_num, phone=phone, tel=tel, sex=sex,age=age, birth=birth, email=email, d_office_id=d_id , level=level, remark=remark, in_data=in_data, d_number=d_number)
        return redirect('doctor:index')




# 查看医生
class look(views.View):
    def get(self,request,e_id):
        # 获取id字段
        e = Doctor.objects.get(id=e_id)
        # 获取所有数据
        doctor_all = Doctor.objects.all()
        return render(request, 'doctor/look.html',{"e":e,"doctor_all":doctor_all})


# 修改医生
class edit(views.View):
    def get(self,request,e_id):
        e = Doctor.objects.get(id=e_id)
        d_all = Departments.objects.all()
        return render(request, 'doctor/edit.html',{"e":e, 'd_all': d_all})

    def post(self,request,e_id):
        doctor_name = request.POST.get("doctor_name")
        card_type = request.POST.get("card_type")
        card_num = request.POST.get("card_num")
        phone = request.POST.get("phone")
        tel = request.POST.get("tel")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        birth = request.POST.get("birth")
        email = request.POST.get("email")
        office = request.POST.get("office")
        level = request.POST.get("level")
        remark = request.POST.get("remark")
        in_data = request.POST.get("in_data")
        d_number = request.POST.get("d_number")
        # 获取id
        e = Doctor.objects.get(id=e_id)
        e.doctor_name = doctor_name
        e.card_type = card_type
        e.card_num = card_num
        e.phone = phone
        e.tel = tel
        e.sex = sex
        e.age = age
        e.email = email
        e.office = office
        e.level = level
        e.remark = remark
        e.d_number = d_number
        e.save()
        return redirect('doctor:index')


def check_verify(request):
    data = {}
    object_value = request.POST.get('object_value')
    data['object_value'] = object_value
    if object_value == '':
        data['status'] = 'ERROR'
        data['message'] = '请填写此选项'
        return JsonResponse(data)
    else:
        data['status'] = 'SUCCESS'
        return JsonResponse(data)

def delete(request, e_id):
    u = Doctor.objects.get(id=e_id)
    u.delete()
    return redirect('doctor:index')