from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from user_profile.models import User
import json


@csrf_exempt
# Create your views here.
def user_profile(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter user id'})
    if request.method == 'GET':
        return JsonResponse({'user_id': pk, 'country': 'Gonduras',
                             'status': 'was online {} minutes ago'.format(random.randint(0, 59))})
    # return JsonResponse({'test': 'Wrong method {}'.format(request.method)})
    return HttpResponseNotAllowed(permited_methods=['GET'], status=405)


@csrf_exempt
@require_http_methods(['GET'])
def user_profile2(request):
    """
    Поиск пользователя, в параметре nick указывается username пользователя, по нему ищем
    Пример: http://127.0.0.1:8000/user_profile/search/?nick=laggy
    :param request: nick
    :return:
    """
    if request.method == 'GET':
        nick = request.GET.get('nick')
        if nick is None:
            return HttpResponseBadRequest('enter user_id')
        else:
            user = list(User.objects.filter(username__contains=nick))
            print(len(user))
            if user:
                final_list = list()
                for one_user in user:
                    final_list.append(one_user.to_json())
                return JsonResponse(final_list, safe=False, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse({}, safe=False)
    return JsonResponse({'strange': 'aha'})

# queryString, брать параметры из request.GET.get()
# делать contains
# возвращать пустой список если нет пользователя
# у юзера сделать метод .toJSON
