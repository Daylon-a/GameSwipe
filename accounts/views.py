from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['psw1']
        password2 = request.POST['psw2']

        if not email:
            raise ValueError('Users must have an email address')
        elif not username:
            raise ValueError('Users must have a username to continue')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save();
                print('user created')
                return redirect('main/')
        else:
            print('user not created: password not matching')
            return redirect('RegisterPage.html')
    else:
        return render(request, 'RegisterPage.html')

def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('main/')
    else:
        return redirect('/')
