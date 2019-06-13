from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    template = loader.get_template('auth/register.html')

    return HttpResponse(template.render({}, request))


def store(request):
    User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
    return redirect(to='users:login')


def signinPage(request):
    template = loader.get_template('auth/login.html')

    return HttpResponse(template.render({}, request))


def signin(request):
    user = authenticate(username=request.POST['name'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(to='competitions:index')

    else:
        return redirect(to='users:login')


def signout(request):
    logout(request)
    return redirect(to='users:login')

def profile(request):
    template = loader.get_template('auth/profile.html')

    return HttpResponse(template.render({}, request))
