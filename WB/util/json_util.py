
from django.http import HttpResponse
import json


def return_json(ctx):
    return HttpResponse(json.dumps(ctx), content_type="application/json")