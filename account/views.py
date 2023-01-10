
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def SignIn(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is None:
            return HttpResponse("username or password is incorrect..")
        else:
            login(user=user, request=request)
            return render(request, 'index.html')

    return redirect('signin')
