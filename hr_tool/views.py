from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .models import User, TPreCareer, TSkill, TAssignExp

# Create your views here.
def employee_list(request):
    return render(request, 'list.html')


def detail(request, pk):
    employee = get_object_or_404(User, id=pk)
    eid = employee.first_name
    if employee.middle_name:
        eid += f'.{employee.middle_name}'
    eid += f'.{employee.last_name}'

    employee_data = [
        ('EID', eid),
        ('社員番号', pk),
        ('氏', employee.last_name),
        ('名', employee.first_name),
        ('キャリア名', employee.career_level.name),
        ('マネジメントレベル', employee.career_level.level),
        ('入社日', employee.join_of),
        ('ホームオフィス', employee.homeoffice.name),
        ('メールアドレス', f'{eid}@accenture.com'),
        ('DTE', employee.dte.name)
    ]

    pre_careers = TPreCareer.objects.filter(eid=pk)
    skills = TSkill.objects.filter(eid=pk)
    assigns = TAssignExp.objects.filter(eid=pk)


    context = {
        'employee_data': employee_data,
        'pre_careers': pre_careers,
        'skills': skills,
        'assigns': assigns
    }

    return render(request, 'detail.html', context)
