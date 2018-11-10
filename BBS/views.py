from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from .models import BBS
from django_comments import models


# Create your views here.
def index(request):
    bbs_list = BBS.objects.all()
    return render(request, 'index.html', {'bbs_list': bbs_list})


def bbs_detail(request, bbs_id):
    bbs = get_object_or_404(BBS, id=bbs_id)
    return render(request, 'bbs_detail.html', {'bbs': bbs})


def sub_comment(request):
    bbs_id = request.POST.get('bbs_id')
    bbs_comment = request.POST.get('comment_content')
    bbs = BBS.objects.get(id=bbs_id)
    models.Comment.objects.create(
        content_type_id=7,
        site_id=1,
        user=request.user,
        comment=bbs_comment,
        object_pk=bbs_id
    )
    return redirect(bbs)


def logout(request):
    user = request.user
    auth.logout(request)
    return HttpResponseRedirect('/bbs')


def bbs_login(request):
    return render(request, 'login.html')


def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/bbs')
    else:
        return render(request, 'login.html', {'login_err': '用户名或密码错误，请重新输入'})
