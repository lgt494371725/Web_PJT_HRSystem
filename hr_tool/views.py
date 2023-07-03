from urllib.parse import unquote

import pandas as pd
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.paginator import Paginator
from django.db import models
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import (AssignExpCreateForm, LoginFrom, PivotTableForm,
                    PreCareerCreateForm, SearchForm, SignUpForm,
                    SkillCreateForm, DetailUpdateForm)
from .models import *
from .para import cross_query, generate_mapping_dict


# Create your views here.
@login_required
def employee_list(request):
    # form = SearchForm(request.GET)
    # employees = User.objects.all()
    # print(form)
    # if form.is_valid():
    #     query = form.cleaned_data['Search']
    #     employees = User.objects.all()
    #     employees = employees.filter(models.Q(id__icontains=query))
    # else:
    #     employees = User.objects.all()
    # paginator = Paginator(employees, 3)
    # page_number = request.GET.get('page', 1)
    # try:
    #     page_number = max(1, int(page_number))
    # except ValueError:
    #     page_number = 1
    # page_obj = paginator.get_page(page_number)
    # context = {
    #     'page_obj': page_obj,
    #     'employees':employees,
    #     'form': form
    # }
    return render(request, 'list.html')

@login_required
def detail(request, pk):
    employee = get_object_or_404(User, id=pk)
    # print("get:", employee)
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
        'pk': pk,
        'employee_data': employee_data,
        'pre_careers': pre_careers,
        'skills': skills,
        'assigns': assigns,
        'employee_id':employee.pk
    }

    return render(request, 'detail.html', context)


# pivot table analysis page
def analysis(request):
    """
    situation:
    1. cate counts: row != None, col = val = None
    2. cate counts: but wrong choose
    3. cate counts: row = col != None, val = None
    4. normal: row=col=val!=None, but val wrong choice
    """
    try:
        mapping_dict = generate_mapping_dict()
        pivot_table = None
        if request.method == 'POST':
            form = PivotTableForm(request.POST)
            if form.is_valid():
                row = form.cleaned_data['row']
                col = form.cleaned_data['column']
                col = col if col else None  # col will be '' if no choose
                val = form.cleaned_data['value']
                agg_func = form.cleaned_data['agg_func']
                # check is cross query
                cand = ['assign_role', 'industry', 'skill']
                if row in cand or col in cand:
                    row_data, col_data, val_data= cross_query(row, col, val)
                else:
                # get records from db based on query
                    row_data = mapping_dict[row][1]
                    col_data = mapping_dict[col][1] if col else None
                    val_data = mapping_dict[val][1] if val else None
                if agg_func == "count":
                    val = "number"
                    val_data = [1]*len(row_data)
                # print("row_data", row_data)
                # print("col_data", col_data)
                # print("val_data", val_data)
                df = pd.DataFrame({row: row_data,
                                col: col_data,
                                val: val_data})
                # print(df)
                # create pivot table
                pivot_table = pd.pivot_table(df, values=val, index=row, columns=col, aggfunc=agg_func, fill_value=0)
                # transform to the html
                # print("table:\n", pivot_table)
                pivot_table = pivot_table.to_html(classes='table table-hover')
                # print(pivot_table)
        else:
            form = PivotTableForm()
        context = {
            'form': form,
            'pivot_table': pivot_table
        }
        return render(request, 'pivot_table.html', context)
    except Exception as e:
        print(type(e))
        message = "Wrong choices!!"+ "Error Type:"+type(e).__name__+", Message:" + str(e)
        context  = {'pivot_table': message}
        return render(request, 'pivot_table.html', context)


def download_file_view(request):
    pivot_table_data = unquote(request.GET.get('pivot_table', ''))

    if pivot_table_data:
        pivot_table_data = pd.read_html(pivot_table_data)[0]
        pivot_table_data = pivot_table_data.to_csv(index=False)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pivot_table.csv"'

        # 将pivot table数据写入响应
        response.write(pivot_table_data)

        return response
    else:
        # 如果没有pivot table数据，则返回错误响应或重定向到其他页面
        return HttpResponse("Error: Pivot table data is missing.", content_type='text/plain')


def edit_precareer(request, pk):
    precareers = TPreCareer.objects.filter(eid=pk)

    context = {
        'pk': pk,
        'precareers': precareers
    }
    return render(request, 'precareer_edit.html', context)


def edit_skill(request, pk):
    skill = TSkill.objects.filter(eid=pk)

    context = {
        'pk': pk,
        'skill': skill
    }
    return render(request, 'skill_edit.html', context)


def add_precareer(request, pk):
    form = PreCareerCreateForm(request.POST or None)
    print(form.data)
    print(dir(form))

    if request.method == 'POST' and form.is_valid():
        employee = get_object_or_404(User, id=pk)
        precareer = form.save(commit=False)
        precareer.eid = employee
        precareer.save()
        return redirect('hr_tool:edit_precareer', pk=pk)

    context = {
        'form': form,
        'eid': pk
    }

    return render(request, 'precareer_form.html', context)


def update_precareer(request, pk):
    precareer = get_object_or_404(TPreCareer, pk=pk)
    form = PreCareerCreateForm(request.POST or None, instance=precareer)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hr_tool:edit_precareer', pk=precareer.eid.id)

    context = {
        'form': form,
        'eid': precareer.eid.id
    }
    return render(request, 'precareer_form.html', context)


def delete_precareer(request, pk):
    precareer = get_object_or_404(TPreCareer, pk=pk)

    if request.method == 'POST':
        precareer.delete()
        return redirect('hr_tool:edit_precareer', pk=precareer.eid.id)

    context = {
        'precareer': precareer,
    }
    return render(request, 'precareer_confirm_delete.html', context)


def edit_assignexp(request, pk):
    assignexps = TAssignExp.objects.filter(eid=pk)

    context = {
        'pk': pk,
        'assignexps': assignexps
    }
    return render(request, 'assignexp_edit.html', context)


def add_assignexp(request, pk):
    form = AssignExpCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        employee = get_object_or_404(User, id=pk)
        assignexp = form.save(commit=False)
        assignexp.eid = employee
        assignexp.save()
        return redirect('hr_tool:edit_assignexp', pk=pk)

    context = {
        'form': form,
        'eid': pk
    }

    return render(request, 'assignexp_form.html', context)


def update_assignexp(request, pk):
    assignexp = get_object_or_404(TAssignExp, pk=pk)
    form = AssignExpCreateForm(request.POST or None, instance=assignexp)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hr_tool:edit_assignexp', pk=assignexp.eid.id)

    context = {
        'form': form,
        'eid': assignexp.eid.id
    }
    return render(request, 'assignexp_form.html', context)


def delete_assignexp(request, pk):
    assignexp = get_object_or_404(TAssignExp, pk=pk)

    if request.method == 'POST':
        assignexp.delete()
        return redirect('hr_tool:edit_assignexp', pk=assignexp.eid.id)

    context = {
        'assignexp': assignexp
    }
    return render(request, 'assignexp_confirm_delete.html', context)


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'hr_user/signupuser.html', {'form': SignUpForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # try:
                homeoffice = MHomeoffice.objects.get(id=request.POST['homeoffice'])
                dte = MDte.objects.get(id=request.POST['dte'])

                print(request.POST)



                user = User.objects.create_user(
                    request.POST['id'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    middle_name=request.POST['middle_name'],
                    password=request.POST['password1'],
                    birthday=request.POST['birthday'],
                    is_hr=('is_hr' in request.POST),
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



def to_json(queryset):
   return [model_to_dict(r) for r in queryset]

def all_skills(request):
    ret = MSkill.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_skillCategories(request):
    ret = MSkillCategory.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def skills_in_categories(request,category_id):
    ret = MSkill.objects.filter(skill_category=category_id)
    return JsonResponse(to_json(ret),safe=False)

def all_careerLevels(request):
    ret = MCareerLevel.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_industries(request):
    ret = MIndustry.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_dtes(request):
    ret = MDte.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_homeoffices(request):
    ret = MHomeoffice.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def dropdown_test(request):
    return render(request, 'dropdown_test.html')

def all_users(request):
    users = []
    for u in User.objects.all():
        users.append({
            '社員番号': u.id,
            'DTE': u.dte.name,
            'ML': u.career_level.level,
            'Joining Date': u.join_of,
            'Home Office': u.homeoffice.name
        })
    return JsonResponse(users, safe=False)

def add_skill(request, pk):
    form = SkillCreateForm(request.POST or None)
    print(form.data)
    print(dir(form))

    if request.method == 'POST' and form.is_valid():
        employee = get_object_or_404(User, id=pk)
        skill = form.save(commit=False)
        skill.eid = employee
        skill.save()
        return redirect('hr_tool:edit_skill', pk=pk)

    context = {
        'form': form
    }

    return render(request, 'skill_form.html', context)

def update_skill(request, pk):
    form = SkillCreateForm(request.POST or None)
    print(form.data)
    print(dir(form))
    if request.method == 'POST' and form.is_valid():
        employee = get_object_or_404(User, id=pk)
        skill = form.save(commit=False)
        skill.eid = employee
        skill.save()
        return redirect('hr_tool:detail', pk=pk)

    context = {
        'form': form
    }

    return render(request, 'skill_form.html', context)


def update_detail(request, pk):
    form = DetailUpdateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        employee = get_object_or_404(User, id=pk)
        print('==========')
        print(form['homeoffice'])
        cl = MCareerLevel.objects.get(id=request.POST['career_level'])
        homeoffice = MHomeoffice.objects.get(id=request.POST['homeoffice'])
        dte = MDte.objects.get(id=request.POST['dte'])

        employee.career_level = cl
        employee.homeoffice = homeoffice
        employee.dte = dte

        employee.save()
        return redirect('hr_tool:detail', pk=pk)

    context = {
        'form': form
    }

    return render(request, 'detail_form.html', context)
