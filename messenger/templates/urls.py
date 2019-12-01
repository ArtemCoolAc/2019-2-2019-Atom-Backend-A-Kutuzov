from django.urls import path
from templates.views import main_sheet

urlpatterns = [
    path('', main_sheet, name = 'main_sheet')
]