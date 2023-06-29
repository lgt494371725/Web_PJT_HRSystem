from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.
def employee_list(request):
    return render(request, 'list.html')


def detail(request, pk):
    return render(request, 'detail.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'hr_user/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('detial')
            except IntegrityError:
                return render(request, 'hr_user/signupuser.html', 
                              {'form': UserCreationForm(), 'error': 'Password didnt match.'}
                              )

def signup(request):
    return render(request, 'hr_tool/signupuser.html')