from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required, user_passes_test
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def test_func(user):
    return user.email.endswith('@qq.com')


# @user_passes_test(test_func)
# @permission_required('login.can_drive')
def drive_car(request):
    # print(request.session.get('_auth_user_id'))
    # print(request.session.get('_auth_user_backend'))
    # print(request.session.get('_auth_user_hash'))
    # pass
    # if not request.user.email.endswith('@qq.com'):
    #     return redirect('/login/login/')
    # if request.user.has_perm('books.add_person'):
    #     print('这是个好人')
    # else:
    #     print('这是个坏蛋')
    return render(request,'login/nouse.html')


def login(request):
    if request.user.is_authenticated:
        message = '不允许重复登录！'
        return render(request,'login/login.html',{'message':message})
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #将用户登录进去
            auth_login(request, user)
            return redirect('/login/drive_car/')
        else:
            message = '用户不存在，或者密码错误！'
            return render(request, 'login/login.html', {'message':message})
    else:
        return render(request, 'login/login.html')


@login_required
def logout(request):
    # 添加你的更多的登出逻辑
    auth_logout(request)
    return redirect('/login/login/')