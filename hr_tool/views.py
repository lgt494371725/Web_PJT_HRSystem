from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PreCareerCreateForm
from .forms import AssignExpCreateForm

from .models import User, TPreCareer, TAssignExp, TProject

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


def edit_precareer(request, pk):
    precareers = TPreCareer.objects.filter(eid=pk)

    context = {
        'pk': pk,
        'precareers': precareers
    }
    return render(request, 'precareer_edit.html', context)


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
    print(form.data)
    print(dir(form))

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
        'assignexp': assignexp,
    }
    return render(request, 'assignexp_confirm_delete.html', context)