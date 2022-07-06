from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Shurl
from random import choice
from string import ascii_letters, digits

def generator():
    return ''.join([choice(ascii_letters + digits) for _ in range(6)])

def index(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_url = generator()
        Shurl.objects.create(long_url=long_url, short_url=short_url)
        context = {
            'new_url': Shurl.objects.all()
        }
        return render(request, 'shurl/index.html', context)
    else:
        context = {
            'new_url': Shurl.objects.all()
        }
        return render(request, 'shurl/index.html', context)

def redirect(request, short_url):
    latest_url = get_object_or_404(Shurl, short_url=short_url)
    return HttpResponseRedirect(latest_url.long_url)
