from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import os
from .models import*


def home(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST.get('age')        
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        birth_day = request.POST['birth_day']
        img = request.FILES.get('img')
        if img:
            if name:
                a = Profile(name=name, image=img, address=address, email=email, Brith_day=birth_day, Gender=gender, phone_number=phone, age=age)
                a.save()
                return redirect('allProf')
            else:
                messages.error(request, "Please Fill Up all fields")
                return redirect('create')
        else:
            a = Profile.objects.create(name=name, address=address, email=email, Brith_day=birth_day, Gender=gender, phone_number=phone, age=age)
            a.save()
            return redirect('allProf')

    return render(request, 'create.html')

@login_required(login_url='login')
def allProf(request):
    seach = request.GET.get('search')
    if seach:
        all_prof = Profile.objects.filter(Q(name__icontains=seach) | Q(email__icontains=seach))
    else:
        all_prof = Profile.objects.all()
    context = {
        'all':all_prof
    }
    return render(request, 'allProf.html', context)

@login_required(login_url='login')
def singleProf(request, id):
    i = Profile.objects.get(id=id)
    return render(request, 'singleProf.html', locals())

@login_required(login_url='login')
def delete(request , id):
    prof = Profile.objects.get(id=id)
    if prof.image != 'defult/profile.jpg':
        os.remove(prof.image.path)
    prof.delete()
    return redirect('allProf')

@login_required(login_url='login')
def updateProfile(request, id):
    prof = Profile.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST.get('age')        
        gender = request.POST['gender']
        phone = request.POST['phone']
        address = request.POST['address']
        birth_day = request.POST['birth_day']
        img = request.FILES.get('img')
        if img:
            if prof.image !='defult/profile.jpg':
                os.remove(prof.image.path)
            prof.image=img
            prof.name=name
            prof.email=email
            prof.age=age
            prof.Gender=gender
            prof.phone_number=phone
            prof.address=address
            prof.Brith_day=birth_day
            prof.address=address
            prof.save()
            messages.success(request, "Update Done")
            return redirect('allProf')
        else:
            prof.name=name
            prof.email=email
            prof.age=age
            prof.Gender=gender
            prof.phone_number=phone
            prof.address=address
            prof.Brith_day=birth_day
            prof.address=address
            prof.save()
            messages.success(request, "Update Done")
            return redirect('allProf')
    return render(request, 'updateProf.html', locals())


