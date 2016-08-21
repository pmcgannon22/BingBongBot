from django.shortcuts import render, render_to_response, redirect
from django.conf import settings

import groupy

# Python logging package
import logging

# Standard instance of a logger with __name__
stdlogger = logging.getLogger(__name__)

#login wrapper
def groupme_login_required(function):
    def wrapper(request, *args, **kw):
        if not request.session.get('token'):
            return redirect('bbmanage.views.login')
        else:
            groupy.config.API_KEY = request.session.get('token')
            return function(request, *args, **kw)
    return wrapper

# Create your views here.

def login(request):
    return render(request, "login.html", {
        'GROUPME_AUTH_URL': settings.GROUPME_AUTH_URL
    })

@groupme_login_required
def bots(request):
    bots = groupy.Bot.list()
    return render(request, "bots.html", {'bots': bots, 'key': groupy.config.API_KEY})

def oauth(request):
    if request.GET.get('access_token'):
        request.session['token'] = request.GET.get('access_token')
        return redirect('/manage')
    else:
        return redirect('bbmanage.views.login')
