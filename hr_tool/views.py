from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import LoginFrom, SignUpForm
from .models import MDte, MHomeoffice, TAssignExp, TPreCareer, TSkill, User


# Create your views here.
@login_required
def employee_list(request):
    return render(request, 'list.html')

@login_required
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
        ('キャリアレベル', employee.career_level.level),
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
        'assigns': assigns,
        'employee_id':employee.pk
    }

    return render(request, 'detail.html', context)

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'hr_user/signupuser.html', {'form': SignUpForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # try:
                homeoffice = MHomeoffice.objects.get(id=request.POST['homeoffice'])
                dte = MDte.objects.get(id=request.POST['dte'])

                user = User.objects.create_user(
                    request.POST['id'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    middle_name=request.POST['middle_name'],
                    password=request.POST['password1'],
                    birthday=request.POST['birthday'],
                    dte=dte,
                    homeoffice=homeoffice
                )
                user.save()
                login(request, user)
                return redirect('hr_tool:detail', pk=request.POST['id'])
            # except IntegrityError:
            #     return render(request, 'hr_user/signupuser.html',
            #                 {'form': SignUpForm(), 'error': 'Password didnt match.'}
            #                 )

def signup(request):
    return render(request, 'hr_tool/signupuser.html')


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = 'hr_user/login.html'

class LogoutView(BaseLogoutView):
    success_url = reverse_lazy('/login')