from django.urls import path
from user_profile.views import user_profile, user_profile2

urlpatterns = [
    path('', user_profile, name='user_profile'),
    path('<int:pk>/', user_profile, name='user_profile'),
    path('prof/<str:pk>/', user_profile2, name='user_profile2'),
    path('search/', user_profile2, name='user_profile2')
]
