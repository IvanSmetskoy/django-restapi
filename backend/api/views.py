import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request.body
    print(request.GET) # url query params
    print(request.POST)  # url query params
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dictionary
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)