from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PreCareerCreateForm

from .models import User, TPreCareer

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
        return redirect('hr_tool:detail', pk=pk)

    context = {
        'form': form
    }

    return render(request, 'precareer_form.html', context)


def update_precareer(request, pk):
    precareer = get_object_or_404(TPreCareer, pk=pk)
    form = PreCareerCreateForm(request.POST or None, instance=precareer)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hr_tool:edit_precareer', pk=precareer.eid.id)

    context = {
        'form': form
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
