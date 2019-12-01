from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
# Create your views here.
def contacts(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter user id'})
    if request.method == 'GET':
        quantity = random.randint(0, 100)
        online = random.randint(0, quantity)
        return JsonResponse({'user id': pk,
                             'quantity of contacts': "{}".format(quantity),
                             'online': "{}".format(online)
                             })
    # return JsonResponse({'test': 'Wrong method {}'.format(request.method)})
    return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)
