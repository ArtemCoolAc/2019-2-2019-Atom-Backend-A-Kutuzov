from django import forms
from chats.models import Chat
from dialog.models import Member
from message.models import Message
from user_profile.models import User


class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('user',)


class NewChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('title', 'is_group_chat', 'topic', 'creator')


class ChooseChat(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('id',)


class MessageForm(forms.ModelForm):
    # chat = forms.ModelChoiceField(queryset=Chat.objects.all())

    class Meta:
        model = Message
        fields = ('user', 'chat', 'content')  # переопределить метод save , тут обновления всех сообщений


class NewChat(forms.Form):
    title = forms.CharField(label='Название чата', max_length=100, required=True)
    is_group_chat = forms.BooleanField(label='Групповой чат')
    topic = forms.CharField(label='Тема', max_length=1000)
    # creator = forms.ChoiceField([user.first_name + user.last_name for user in User.objects.all()])
    creator = forms.ChoiceField(label='Создатель', required=True,
                                choices=[tuple([user, user.first_name + ' ' + user.last_name]) for user in
                                         list(User.objects.all())])
    user = forms.ChoiceField(label='Участник', required=True,
                             choices=[tuple([user, user.first_name + ' ' + user.last_name]) for user in
                                      list(User.objects.all())])

    def save(self):
        elements = self.cleaned_data
        for_chat = {'title': elements['title'], 'is_group_chat': elements['is_group_chat'], 'topic': elements['topic'], 'creator': elements['creator']}
        membership = {}
        Chat.objects.create(**for_chat)
        return Chat.objects.create(**self.cleaned_data)
