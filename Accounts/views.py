from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required


# Create your views here.
def log_in(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pass1 = request.POST.get('pass')
        if name:
            user = authenticate(username = name, password = pass1)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Input username and password")

    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 == pass2:
            if User.objects.filter(username = name).exists():
                messages.error(request, "Already username is taken")
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Already email is taken")
            else:
                user = User.objects.create(username=name, first_name=f_name, last_name=l_name, email=email, password=pass1)
                user.set_password(pass1)
                messages.success(request, "User Registration Done")
                return redirect('login')
        else:
            messages.error(request, "Password No Matched")
    return render(request, 'registration.html')

def log_out(request):
    user=request.user
    logout(request)
    return redirect('login')