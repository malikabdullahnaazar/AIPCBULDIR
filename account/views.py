
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.


def HomePage(request):
    pass


def Signuppage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(
            username=uname, email=email, password=password),
        return redirect('signin')
    return render(request, 'signupfrom.html')


def SignIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect..")

    return render(request, 'loginForm.html')


def homepage(request):

    return render(request, 'index.html')
