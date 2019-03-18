# coding:utf-8

import os
import time

from WB.util.json_util import return_json


def upload_image(request):
    ctx = {}
    if request.method == 'POST':
        current_time = int(round(time.time() * 1000))
        print(current_time)
        upload_file = request.FILES.get('file')
        f = open(os.path.join("./upload/", "%s.jpg" % current_time), 'wb')
        for chunk in upload_file.chunks():
            f.write(chunk)
        f.close()
        ctx['code'] = 0
        ctx['msg'] = "success"
        ctx['url'] = "/upload/%s.jpg" % current_time

    return return_json(ctx)
