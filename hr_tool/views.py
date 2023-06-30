from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PreCareerCreateForm
from .forms import SkillCreateForm

from .models import User, TPreCareer
from .models import User, TSkill

def employee_list(request):
    return render(request, 'list.html')


def detail(request, pk):
    employee = get_object_or_404(User, id=pk)
    precareers = TPreCareer.objects.filter(eid=employee)

    context = {
        'pk': pk,
        'precareers': precareers
    }
    
    return render(request, 'detail.html', context)

def detail(request, pk):
    employee = get_object_or_404(User, id=pk)
    skill = TPreCareer.objects.filter(eid=employee)

    context = {
        'pk': pk,
        'skill': skill
    }
    return render(request, 'detail.html', context)
    

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
        return redirect('hr_tool:detail', pk=pk)

    context = {
        'form': form
    }

    return render(request, 'precareer_form.html', context)

def add_skill(request, pk):
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