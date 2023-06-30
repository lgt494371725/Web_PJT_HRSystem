from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PreCareerCreateForm
from .forms import AssignExpCreateForm

from .models import User, TPreCareer, TAssignExp, TProject

# Create your views here.
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
        'pk': pk,
        'form': form
    }

    return render(request, 'add_precareer_form.html', context)


def precareer(request, pk):
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
        'pk': pk,
        'precareer_list': TPreCareer.objects.all(),
        'form': form
    }

    return render(request, 'precareer_form.html', context)


def update_precareer(request, pk):
    # フォームに、取得したDayを紐付ける
    form = PreCareerCreateForm(request.POST or None)
    print(form.data)
    print(dir(form))

    # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hr_tool:detail', pk=pk)
    
    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'pk': pk,
        'form': form
    }
    return render(request, 'update_precareer_form.html', context) 


def delete_precareer(request, pk):
    # urlのpkを基に、Dayを取得

    # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
    if request.method == 'POST':
        PreCareerCreateForm.delete()
        return redirect('hr_tool:detail', pk=pk)
    
    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'pk': pk
    }
    return render(request, 'delete_precareer_form.html', context)




def add_assignexp(request, pk):
    form = AssignExpCreateForm(request.POST or None)
    print(form.data)
    print(dir(form))

    if request.method == 'POST' and form.is_valid():
        employee = get_object_or_404(User, id=pk)
        precareer = form.save(commit=False)
        precareer.eid = employee
        precareer.save()
        return redirect('hr_tool:detail', pk=pk)

    context = {
        'pk': pk,
        'form': form
    }

    return render(request, 'add_assignexp_form.html', context)


def update_assignexp(request, pk):
    form = AssignExpCreateForm(request.POST or None)
    print(form.data)
    print(dir(form))

    if request.method == 'POST' and form.is_valid():
        employee = get_object_or_404(User, id=pk)
        precareer = form.save(commit=False)
        precareer.eid = employee
        precareer.save()
        return redirect('hr_tool:detail', pk=pk)

    context = {
        'pk': pk,
        'form': form
    }

    return render(request, 'update_assignexp_form.html', context)


def assignexp(request, pk):
    context = {
        'pk': pk,
        'assign_list': AssignExpCreateForm.objects.all(),
    }
    return render(request, 'assignexp_form.html', context)


def delete_assignexp(request, pk):
    form = AssignExpCreateForm(request.POST or None)
    print(form.data)
    print(dir(form))

    if request.method == 'POST' and form.is_valid():
        employee = get_object_or_404(User, id=pk)
        precareer = form.save(commit=False)
        precareer.eid = employee
        precareer.save()
        return redirect('hr_tool:detail', pk=pk)

    context = {
        'pk': pk,
        'form': form
    }

    return render(request, 'delete_assignexp_form.html', context)