from django.shortcuts import render
from .models import User
from .forms import SearchForm

# Create your views here.
def employee_list(request):
    employees = User.objects.all()
    context = {
        'employees':employees
    }
    
    return render(request, 'list.html',context)


def detail(request, pk):
    return render(request, 'detail.html')

def index(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['id']
        employees = User.objects.filter(id=query)
    else:
        print("!!!error:",form.errors)
    context = {
        'employees': employees,
        'form': form

    }
    return render(request, 'hr_tool/list.html',context)