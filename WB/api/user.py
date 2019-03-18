from django.core import serializers
from django.db.models import Q

from Model.models import User
from WB.util.json_util import return_json
import json


def login(request):
    ctx = {}
    if request.method == 'POST':
        account = request.POST.get("account", "")
        password = request.POST.get("password", "")
        user_list = User.objects.filter(Q(username=account) | Q(mobile=account), password=password)
        if len(user_list) != 0:
            user = user_list[0]
            ctx['code'] = 0
            ctx['msg'] = "login success"
            ctx['data'] = {'id': user.id,
                           'username': user.username,
                           'mobile': user.mobile,
                           'email': user.email,
                           'code': user.code
                           }
        else:
            ctx['code'] = 1
            ctx['msg'] = "account or password error"

    return return_json(ctx)


def register(request):
    ctx = {}
    if request.method == 'POST':
        username = request.POST.get("username", "")
        mobile = request.POST.get("mobile", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")
        if username == "":
            ctx['code'] = 1
            ctx['msg'] = "username is no null"
        elif password == "":
            ctx['code'] = 1
            ctx['msg'] = "password is no null"
        elif mobile == "":
            ctx['code'] = 1
            ctx['msg'] = "mobile is no null"
        elif len(mobile) != 11:
            ctx['code'] = 1
            ctx['msg'] = "mobile's length is must achieve 11"
        elif email == "":
            ctx['code'] = 1
            ctx['msg'] = "email is no null"
        else:
            user_list = User.objects.filter(username=username, mobile=mobile)
            if len(user_list) > 0:
                ctx['code'] = 1
                ctx['msg'] = "current user is exist"
            else:
                user = User(username=username, mobile=mobile, password=password, email=email)
                user.save()
                ctx['code'] = 0
                ctx['msg'] = "register success"

    return return_json(ctx)
