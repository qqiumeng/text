from django.shortcuts import render, HttpResponse, redirect
from django import views
from Resource.forms import *
from django.core.paginator import Paginator


# Create your views here.


class index(views.View):
    """
    首页展示
    """

    def get(self, request):
        """
        信息展示以及分页功能
        :param request: 必传参数
        :return: 页面以及信息参数
        """
        all_manager = Resource.objects.all()
        limit = 5
        paginator = Paginator(all_manager, limit)  # 按每页5条分页
        page = request.GET.get('page', '1')  # 默认跳转到第一页
        result = paginator.page(page)  # 前5条信息
        return render(request, 'Resource/index.html', {'all': result})

    def post(self, request):
        """
        实现信息的查询
        :param request:
        :return: 查询到的数据
        """
        r_name = request.POST.get('r_name')
        try:
            u = Resource.objects.filter(r_name=r_name)
        except:
            return HttpResponse('您想要查找的资源不存在')
        else:
            return render(request, 'Resource/index.html', {'u': u})


class add(views.View):
    """
    添加数据功能
    """

    def get(self, request):
        return render(request, 'Resource/add.html')

    def post(self, request):
        """
        添加资源，并进行判断
        :param request:
        :return:
        """
        r_name = request.POST.get('r_name')
        url = request.POST.get('url')
        result = request.POST.get('result')
        if Resource.objects.filter(r_name=r_name):
            return render(request, 'Resource/add.html', {'erro': '此资源已存在，请重新输入'})
        else:
            Resource.objects.create(r_name=r_name, url=url, result=result)
            return redirect('Resource:index')


class edit(views.View):
    """
    编辑功能，相当于更改
    """

    def get(self, request, u_id):
        """
        根据网页上的参数获取到信息返回给页面
        :param request:
        :param u_id: 传的参数
        :return: 获取到的信息
        """
        u = Resource.objects.get(id=u_id)
        return render(request, 'Resource/edit.html', {'u': u})

    def post(self, request, u_id):
        """
        获取到当前信息的id，对当前信息进行更改
        :param request:
        :param u_id: 传的参数
        :return: 跳转的页面
        """
        r_name = request.POST.get('r_name')
        url = request.POST.get('url')
        result = request.POST.get('result')
        u = Resource.objects.get(id=u_id)
        u.r_name = r_name
        u.result = result
        u.url = url
        u.save()
        return redirect('Resource:index')


class drop(views.View):
    """
    删除资源
    """

    def get(self, request, u_id):
        u = Resource.objects.get(id=u_id)
        u.delete()
        return redirect('Resource:index')

def dropall(request):
    ss=request.POST.get('ss')
    list1=[]
    for i in list(ss):
        if i !=',':
            list1.append(i)
    for a in list1:
        Resource.objects.get(id=a).delete()
        return redirect('Resource:index')
