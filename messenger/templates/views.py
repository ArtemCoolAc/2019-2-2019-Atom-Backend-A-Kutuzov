from django.shortcuts import render


def main_sheet(request):
    return render(request, 'Main.html')
