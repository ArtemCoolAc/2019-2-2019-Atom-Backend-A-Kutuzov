from user_profile.models import User


def insert_users():
    user = User.objects.create(first_name='Алексаднр', second_name='Лавренов', nick='laggy', avatar='smth.png')