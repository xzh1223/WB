from django.conf.urls import url
from WB.api import user, blog, upload, focus

urlpatterns = [
    url(r'^wb/user/login$', user.login),
    url(r'^wb/user/register$', user.register),
    url(r'^wb/blog/refresh_blog$', blog.refresh_blog),
    url(r'^wb/blog/get_blog_list$', blog.get_blog_list),
    url(r'^wb/upload/upload_image$', upload.upload_image),
    url(r'^wb/focus/get_focus_list$', focus.get_focus_list),
    url(r'^wb/focus/add_focus$', focus.add_focus),
    url(r'^wb/focus/update_focus$', focus.update_focus),
    url(r'^wb/focus/delete_focus$', focus.delete_focus),
]
