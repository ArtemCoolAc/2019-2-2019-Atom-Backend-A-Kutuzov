from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
# Create your views here.
def dialog(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter chat page id'})
    if request.method == 'GET':
        quantity = random.randint(1, 100)
        last_hour = random.randint(0, 23)
        last_minute = random.randint(0, 59)
        return JsonResponse({'chat page id': pk, 'quantity of messages': '{}'.format(quantity),
                             'last_message': '{}:{}'.format(last_hour, last_minute)})
    # return JsonResponse({'test': 'Wrong method {}'.format(request.method)})
    return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)
