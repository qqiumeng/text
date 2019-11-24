from django.shortcuts import render, HttpResponse, redirect
from django import views
from Users.forms import *
from django.core.paginator import Paginator
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from django.utils.six import BytesIO


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
        all_manager = ManageUsers.objects.all()
        limit = 5
        paginator = Paginator(all_manager, limit)  # 按每页5条分页
        page = request.GET.get('page', '1')  # 默认跳转到第一页
        result = paginator.page(page)
        return render(request, 'Users/index.html', {'all': result})

    def post(self, request):
        """
        实现信息的查询
        :param request:
        :return: 查询到的数据
        """
        login_name = request.POST.get('login_name')
        try:
            u = ManageUsers.objects.filter(login_name=login_name)
        except:
            return HttpResponse('您想要查找的用户不存在，请重新输入')
        else:
            return render(request, 'Users/index.html', {'u': u})


class addUser(views.View):
    """
    添加用户功能
    """

    def get(self, request):
        return render(request, 'Users/addUser.html')

    def post(self, request):
        """
        添加用户，并进行判断
        :param request:
        :return:
        """
        login_name = request.POST.get('login_name')
        password = request.POST.get('password')
        real_name = request.POST.get('real_name')
        email = request.POST.get('email')
        state = request.POST.get('state')
        role = request.POST.get('role')
        if ManageUsers.objects.filter(login_name=login_name):
            return render(request, 'Users/addUser.html', {'erro': '此用户已存在，请重新输入'})
        elif len(role) <= 1:
            return HttpResponse('字段不能为空，请重新输入')
        else:
            ManageUsers.objects.create(login_name=login_name, password=password, real_name=real_name, email=email,
                                       state=state, role=role)
            return redirect('Users:index')


class editUser(views.View):
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
        u = ManageUsers.objects.get(id=u_id)
        return render(request, 'Users/editUser.html', {'u': u})

    def post(self, request, u_id):
        """
        获取到当前信息的id，对当前信息进行更改
        :param request:
        :param u_id: 传的参数
        :return: 跳转的页面
        """
        password = request.POST.get('password')
        real_name = request.POST.get('real_name')
        email = request.POST.get('email')
        state = request.POST.get('state')
        role = request.POST.get('role')

        if len(role) <= 1:
            return HttpResponse('角色不能为空，请重新输入')
        else:
            u = ManageUsers.objects.get(id=u_id)
            u.password = password
            u.real_name = real_name
            u.email = email
            u.state = state
            u.role = role
            u.save()
            return redirect('Users:index')


class password(views.View):
    """
    更改密码功能
    """

    def get(self, request):
        return render(request, 'Users/password.html')

    def post(self, request):
        """
        获取到当前登陆的用户，更改密码
        :param request:
        :return:
        """
        password = request.POST.get('password')
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')
        u_id = request.session.get('u_id')
        u = ManageUsers.objects.get(id=u_id)
        if u.password == password:
            if len(pw1) != 0 or len(pw2) != 0:
                if pw1 == pw2:
                    u.password = pw1
                    u.save()
                    return redirect('Users:login')
                else:
                    return render(request, 'Users/password.html', {'erro': '两次密码输入不一致，请重新输入'})
            else:
                return render(request, 'Users/password.html', {'erro': '密码不能为空'})
        else:
            return render(request, 'Users/password.html', {'erro': '密码不正确，请重新输入'})


class login(views.View):
    """
    用户登录功能
    """

    def get(self, request):
        return render(request, 'Users/login.html')

    def post(self, request):
        """
        用户登录，并对登录信息进行验证
        :param request:
        :return:
        """
        f = UserInfo(request.POST)

        if f.is_valid():
            login_name = f.cleaned_data.get('login_name')
            password = f.cleaned_data.get('password')
            # 获取用户输入的验证码
            vcode_input = request.POST.get('vcode')
            # 获取session中存储的验证码
            vcode_session = request.session.get('verifycode')
            # 进行验证码的校验
            if vcode_input != vcode_session:
                # 验证码错误
                return render(request, 'Users/login.html', {'erro': '验证码不正确，请重新输入'})
            else:
                try:
                    u = ManageUsers.objects.get(login_name=login_name, password=password)
                    request.session['u_id'] = u.id
                    return render(request, 'hospital/index.html', {'login_name': login_name})
                except:
                    return render(request, 'Users/login.html', {'erro': '用户名或密码错误，请重新输入'})
        else:
            return HttpResponse('登录失败')


class drop(views.View):
    """
    删除用户
    """

    def get(self, request, u_id):
        u = ManageUsers.objects.get(id=u_id)
        u.delete()
        return redirect('Users:index')


def dropall(request):
    ss = request.POST.get('ss')
    list1 = []
    for i in list(ss):
        if i != ',':
            list1.append(i)
    for a in list1:
        ManageUsers.objects.get(id=a).delete()
        return redirect('Users:index')


# 生成验证码
# random character
def rndChar():
    return chr(random.randint(65, 90))


# random color 1
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# random color 2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 * 60
def draw(request):
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # create Font object
    myfont = ImageFont.truetype('E:\demo.py\数据分析内容\\01-入门/苹方粗体.ttf', 36)

    # create Draw object
    draw = ImageDraw.Draw(image)

    # fill in every pixel
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor1())

    # output the text
    code1 = ''
    for t in range(4):
        tmpChar = rndChar()
        draw.text((60 * t + 10, 10), tmpChar, font=myfont, fill=rndColor2())
        code1 += tmpChar

    # fuzzy

    image = image.filter(ImageFilter.BLUR)
    # image.save('../imgs/test1.jpg', 'jpeg')
    request.session['verifycode'] = code1
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    image.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
