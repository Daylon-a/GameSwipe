from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['psw1']
        password2 = request.POST['psw2']
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
                return redirect('/')
        else:
            print('user not created: password not matching')
            return redirect('RegisterPage.html')
    else:
        return render(request, 'RegisterPage.html')

def login(request):
    return render(request, 'LoginPage.html')