from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pmpapp.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'pmpapp/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('pmp:index'))


def register(request):
    registered = False
    if request.method == 'POST':
        loginForm = LoginForm(data=request.POST)
        registerForm = RegisterForm(data=request.POST)
        if loginForm.is_valid() and registerForm.is_valid():
            user = loginForm.save()
            user.set_password(user.password)
            user.save()
            userInfo = registerForm.save(commit=False)
            userInfo.user = user
            if 'profile_picture' in request.FILES:
                userInfo.profile_picture = request.FILES['profile_picture']
            userInfo.save()
            registered = True
        else:
            print(loginForm.errors, registerForm.errors)
    else:
        loginForm = LoginForm()
        registerForm = RegisterForm()
    return render(request, 'pmpapp/register.html',
                  {'loginForm': loginForm,
                   'registerForm': RegisterForm,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('pmp:index'))
            else:
                print('User account is inactive')
        else:
            print('login failed for user: {}'.format(username))
            return HttpResponse('Invalid login credentials')
    else:
        return render(request, 'pmpapp/login.html', {})
