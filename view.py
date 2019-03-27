from django.http omport HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse('index')


def login(request):
    return redirect('/index')
