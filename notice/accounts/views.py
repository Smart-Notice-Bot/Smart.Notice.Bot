from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from accounts.models import User
from django.contrib import auth

import logging
logger=logging.getLogger(__name__)
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create(username=request.POST['username'], email=request.POST['email'], dept=request.POST['dept'])
            user.set_password(request.POST['password1'])
            user.save()
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logger.info('username = {}'.format(username))

        user = auth.authenticate(request, username=username, password=password)
        logger.info('user = {}'.format(user))
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
