from chats.views import chat_list, create_chat, list_chats, messages_list, send_message, read_message
from django.urls import path

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<int:pk>/', chat_list, name='chat_list'),
    path('new/', create_chat, name='create_chat'),
    path('user_chats/<str:pk>/', list_chats, name='list_chats'),
    path('messages/<int:pk>', messages_list, name='messages_list'),
    path('send/', send_message, name='send_message'),
    path('read/<int:pk1>/<str:pk2>', read_message, name='read_message')
]
