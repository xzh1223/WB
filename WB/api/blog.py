# coding:utf-8

from Model.models import MyBlog
from WB.util.reptile_util import get_html
from WB.util.json_util import return_json


def refresh_blog(request):
    if request.method == 'POST':
        ctx = {}
        blog = get_html('https://blog.csdn.net/github_38613243')
        url_list = blog['url']
        title_list = blog['title']
        content_list = blog['content']
        description_list = blog['description']
        date_list = blog['date']
        i = 0
        for i in range(len(url_list) - 1):
            MyBlog.objects.filter(url=url_list[i]).delete()
            my_blog = MyBlog(url=url_list[i], content=content_list[i], description=description_list[i],
                             title=title_list[i], create_time=date_list[i])
            my_blog.save()
            i = i + 1
        if i > 0:
            ctx['code'] = 0
            ctx['msg'] = '刷新成功'
        else:
            ctx['code'] = 0
            ctx['msg'] = '没有数据'
    return return_json(ctx)


def get_blog_list(request):
    print("读取博客数据-->")
    if request.method == 'POST':
        # page = request.POST.get("page", 1)
        # page_size = request.POST.get("page_size", 10)
        ctx = {}
        temp_list = []
        # blog_list = MyBlog.objects.all()[(int(page) * page_size - page_size):(int(page) * page_size)]
        blog_list = MyBlog.objects.all()
        if len(blog_list) > 0:
            for blog in blog_list:
                b = {'id': blog.id, 'title': blog.title, 'description': blog.description, 'content': blog.content,
                     'url': blog.url, 'create_time': blog.create_time}
                temp_list.append(b)
            ctx['code'] = 0
            ctx['msg'] = "获取成功"
            ctx['data'] = temp_list
        else:
            ctx['code'] = 0
            ctx['msg'] = "暂无数据"
            ctx['data'] = []
    return return_json(ctx)
