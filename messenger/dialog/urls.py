from dialog.views import dialog
from django.urls import path

urlpatterns = [
    path('', dialog, name='dialog'),
    path('<int:pk>/', dialog, name='dialog'),
]