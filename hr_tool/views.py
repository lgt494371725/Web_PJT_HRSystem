from django.shortcuts import render
from .models import User
from .forms import SearchForm
from django.db import models

# Create your views here.
def employee_list(request):
    form = SearchForm(request.GET)
    employees = User.objects.all() 
    print(form)
    if form.is_valid():
        query = form.cleaned_data['Search']
        print('abc',query)
        employees = User.objects.all() 
        employees = employees.filter(models.Q(id__icontains=query))
    else:
        print("!!!error:",form.errors)
        employees = User.objects.all() 
    context = {
        'employees':employees,
        'form': form
    }
    return render(request, 'list.html',context)


def detail(request, pk):
    return render(request, 'detail.html')

# def index(request):
#     form = SearchForm(request.GET)
#     print(form)
#     if form.is_valid():
#         query = form.cleaned_data['search']
#         employees = User.objects.filter(id=query)
#         employees = User.objects.all()
#     else:
#         print("!!!error:",form.errors)
#     context = {
#         'employees': employees,
#         'form': form
#     }
#     return render(request, 'hr_tool/list.html',context)