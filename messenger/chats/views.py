from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Chat
from django.template import RequestContext
import datetime
from django import forms
from dialog.models import Member
from message.models import Message
from user_profile.models import User
from .forms import MessageForm, MembersForm, NewChatForm, ChooseChat, NewChat


# from messenger.user_profile.models import User

@csrf_exempt
def chat_list(request, pk=None):
    if pk is None:
        return JsonResponse({'msg': 'enter chat_id'})
    if request.method == 'GET':
        return JsonResponse({'chat_id': pk, 'members': 2})
    # return JsonResponse({'test': 'Wrong method {}'.format(request.method)}, status=405)
    return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def create_chat(request):
    if request.method == 'POST':
        chat_form = NewChatForm(request.POST)
        member_form = MembersForm(request.POST)
        if chat_form.is_valid() and member_form.is_valid():
            current_chat = chat_form.save()
            # full = member_form.save(commit=False)
            # full.chat = current_chat
            # full.save()
            Member.objects.create(user=current_chat.creator, chat=current_chat)  # JsonResponse обязательно
            return JsonResponse({'smth': 'OK'})
    else:
        chat_form = NewChatForm()
        member_form = MembersForm()
    return render_to_response('new_chat.html', {'chat_form': chat_form, 'member_form': member_form}, )


@csrf_exempt
def list_chats(request, pk=None):
    """
    Поиск чатов по нику. Пример http://127.0.0.1:8000/chats/user_chats/frostics/
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'GET':
        print(pk)
        if pk is None:
            # return JsonResponse({'message': 'specify user id'}) #error 400
            return HttpResponseBadRequest('Specify user!')
        # user = User.objects.all().filter(username=pk)[0] #try  except; можно проверить .first; get_objects_or_404
        user = get_object_or_404(User.objects.filter(username=pk))
        membership = Member.objects.all().filter(user=user.id)
        chats = list()
        for member in membership:
            chats.append(member.chat)
        response = dict()
        for chat in chats:
            response['chat {}'.format(chat.id)] = {
                'user': user.first_name + ' ' + user.last_name,
                'is_group_chat': chat.is_group_chat,
                'topic': chat.topic or 'absent',
                'creator': chat.creator.first_name + ' ' + chat.creator.last_name,
            }
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)


@csrf_exempt
def messages_list(request, pk=None):
    """
    Список сообщений пользователя. Пример: http://127.0.0.1:8000/chats/messages/3
    :param request:
    :param pk: id пользователя
    :return:
    """
    if request.method == 'GET':
        if pk is None:
            return HttpResponseBadRequest('enter chat id')
        current_chat = get_object_or_404(Chat, id=pk)
        chat_messages = Message.objects.filter(chat=current_chat) # related
        response = dict()
        for message in chat_messages:
            response['message {}'.format(message.id)] = {
                'user': message.user.to_json(),
                'chat': message.chat.to_json(),
                'content': message.content,
                'added_at': message.added_at
            }
        return JsonResponse(response)
    return HttpResponseNotAllowed(permitted_methods=['GET'], status=405)


@csrf_exempt
def send_message(request):
    """
    Отправка сообщения
    :param request:
    :return:
    """
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        # print(message_form)
        if message_form.is_valid():
            message = message_form.save()
            Chat.objects.all().filter(id=message.chat_id).update(last_message=message.content)
            # print('Before')
            # print(str(message.user) + ' ' + str(message.chat) + ' ' + str(message.content))
            # Message.objects.create(user=message.user, chat=message.chat, content=message.content)
            # print('After')
            # Chat.objects.all().filter(id=message.chat)[0].update(last_message=message.content)
            # Message.objects.select_related().filter(chat=message.chat).update(last_message=message.content)

    else:
        message_form = MessageForm()
    return render_to_response('send_message.html', {'message_form': message_form})


# def read_message(request, pk1=None, pk2=None):
#     if request.method == 'GET':
#         chat = Chat.objects.all().filter(id=pk1)
#         print(chat[0])
#         if chat.exists():
#             user = User.objects.all().filter(username=pk2)
#             print(user[0])
#             if user.exists():
#                 member = Member.objects.all().filter(user=user[0]) and Member.objects.all().filter(chat=chat[0])
#                 # member = Member.objects.all().filter(chat=chat[0])
#                 print(member[0])
#                 if member.exists():
#                     last_message = Message.objects.all().filter(user=user[0]) and Message.objects.all().filter(chat=chat[0])
#                     # last_message = Message.objects.all().filter(chat=chat[0])
#                     if last_message.exists():
#                          Member.objects.all().filter(user=user[0]) and Member.objects.all().filter(chat=chat[0]).update(last_read_message=last_message[0])
#                         # Member.objects.all().filter(chat=chat[0]).update(last_read_message=last_message[0])
#     return JsonResponse({'dzfse': 'zzzzzfsef'})


def read_message(request, pk1=None, pk2=None):
    """
    Читаем все сообщения по заходу в чат. Пример: http://127.0.0.1:8000/chats/read/3/frostics
    :param request:
    :param pk1: чат id
    :param pk2: ник
    :return:
    """
    if request.method == 'GET':
        chat = get_object_or_404(Chat, id=pk1)
        user = get_object_or_404(User, username=pk2)
        member = Member.objects.filter(user=user, chat=chat)
        # member = list(set(get_list_or_404(Member.objects.filter(user=user))) & set(get_list_or_404(
        #     Member.objects.filter(chat=chat))))[0]
        last_message = Message.objects.filter(user=user).first()
        member.update(last_read_message=last_message)
        return JsonResponse({})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET'])
