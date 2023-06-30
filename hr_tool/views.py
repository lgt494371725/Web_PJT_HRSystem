from django.shortcuts import render, get_object_or_404, redirect
from .models import User, TPreCareer, TSkill, TAssignExp
from django.http import HttpResponse
from .models import *
import pandas as pd
from .forms import PivotTableForm, SearchForm
from .para import mapping_dict
from urllib.parse import unquote
from django.db import models
from django.core.paginator import Paginator

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
        employees = User.objects.all() 
    paginator = Paginator(employees, 2) 
    page_number = request.GET.get('page', 1)
    try:
        page_number = max(1, int(page_number))
    except ValueError:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'employees':employees,
        'form': form
    }
    return render(request, 'list.html',context)


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
        pivot_table = None
        if request.method == 'POST':
            form = PivotTableForm(request.POST)
            if form.is_valid():
                row = form.cleaned_data['row']
                col = form.cleaned_data['column']
                col = col if col else None  # col will be '' if no choose
                val = form.cleaned_data['value']
                agg_func = form.cleaned_data['agg_func']
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
                # # create pivot table
                pivot_table = pd.pivot_table(df, values=val, index=row, columns=col, aggfunc=agg_func, fill_value=0)
                # # transform to the html
                # print("table:\n", pivot_table)
                pivot_table = pivot_table.to_html()
        else:
            form = PivotTableForm()
        context = {
            'form': form,
            'pivot_table': pivot_table
        }
        return render(request, 'pivot_table.html', context)
    except Exception as e:
        print(f"Wrong choices!! {type(e)}, error message:", e)
        return render(request, 'pivot_table.html', {'pivot_table': e})
    

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