from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def iletisim(request):
    return render(request, 'pages/iletisim.html', context={})


def anasayfa(request):
    return render(request, 'pages/anasayfa.html', context={})
