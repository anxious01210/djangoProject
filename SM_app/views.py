from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from SM_app.EmailBackEnd import EmailBackEnd


def demo(request):
    return render(request, 'demo.html')


def show_login_page(request):
    return render(request, 'login_page.html')


def doLogin(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method Not Allowed</h2>')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponse('Email: "' + request.POST.get('email') + '" .-^-. Password: "' + request.POST.get('password')+'"')
        else:
            return HttpResponse('Invalid Login')


def get_user_details(request):
    if request.user is not None:
        return HttpResponse('User : ' + request.user.email + ' usertype : ' + str(request.user.user_type))
    else:
        return HttpResponse('Please Login First')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
