# coding:utf-8
from Model.models import Focus
from WB.util.json_util import return_json


# 获取聚焦列表
def get_focus_list(request):
    ctx = {}
    temp_list = []
    if request.method == 'POST':
        user_id = request.POST.get("user_id", 0)
        if user_id == 0:
            ctx['code'] = 1
            ctx['msg'] = "没有获取到用户ID"
        else:
            focus_list = Focus.objects.filter(user_id=user_id)
            if len(focus_list) > 0:
                for focus in focus_list:
                    create_time = focus.create_time.strftime("%Y-%m-%d %H:%M:%S")
                    f = {'id': focus.id, 'title': focus.title, 'content': focus.content,
                         'create_time': create_time,'time':focus.time, 'status': focus.status}
                    temp_list.append(f)
                ctx['code'] = 0
                ctx['msg'] = "获取成功"
                ctx['data'] = temp_list
            else:
                ctx['code'] = 0
                ctx['msg'] = "暂无数据"
                ctx['data'] = []

    return return_json(ctx)


# 添加聚焦
def add_focus(request):
    ctx = {}
    if request.method == 'POST':
        user_id = request.POST.get("user_id", 0)
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        time = request.POST.get("time", 0)
        if user_id == 0:
            ctx['code'] = 1
            ctx['msg'] = "没有获取到用户ID"
        elif time == 0:
            ctx['code'] = 1
            ctx['msg'] = "请输入时长"
        else:
            focus = Focus(title=title, content=content, time=time, user_id=user_id)
            focus.save()
            ctx['code'] = 0
            ctx['msg'] = "添加成功"
    return return_json(ctx)


# 修改聚焦
def update_focus(request):
    ctx = {}
    if request.method == 'POST':
        user_id = request.POST.get("user_id", 0)
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        time = request.POST.get("time", 0)
        f_id = request.POST.get("id", 0)
        if id == 0:
            ctx['code'] = 1
            ctx['msg'] = "没有获取到参数ID"
        elif user_id == 0:
            ctx['code'] = 1
            ctx['msg'] = "没有获取到用户ID"
        elif time == 0:
            ctx['code'] = 1
            ctx['msg'] = "请输入时长"
        else:
            focus = Focus(id=f_id, title=title, content=content, time=time, user_id=user_id)
            focus.save()
            ctx['code'] = 0
            ctx['msg'] = "修改成功"
    return return_json(ctx)


# 删除聚焦
def delete_focus(request):
    ctx = {}
    if request.method == 'POST':
        f_id = request.POST.get("id", 0)
        if id == 0:
            ctx['code'] = 1
            ctx['msg'] = "没有获取到参数ID"
        else:
            focus = Focus.objects.filter(id=f_id).first()
            if focus is None:
                ctx['code'] = 1
                ctx['msg'] = "未查到这条记录"
            else:
                focus.delete()
                ctx['code'] = 0
                ctx['msg'] = "删除成功"
    return return_json(ctx)


# 修改聚焦状态
def finish_focus(request):
    ctx = {}
    if request.method == 'POST':
        f_id = request.POST.get("id", 0)
        if id == 0:
            ctx['code'] = 1
            ctx['msg'] = "没有获取到参数ID"
        else:
            focus = Focus.objects.filter(id=f_id).first()
            if focus is None:
                ctx['code'] = 1
                ctx['msg'] = "未查到这条记录"
            else:
                if focus.status == 0:
                    focus.status = 1
                else:
                    focus.status = 0
                focus.save()
                ctx['code'] = 0
                ctx['msg'] = "成功"

    return return_json(ctx)
