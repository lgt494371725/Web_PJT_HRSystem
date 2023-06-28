from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import pandas as pd
from .forms import PivotTableForm


def employee_list(request):
    return render(request, 'list.html')


def detail(request, pk):
    return render(request, 'detail.html')

# pivot table analysis page
def analysis(request):
    pivot_table = None
    if request.method == 'POST':
        form = PivotTableForm(request.POST)
        if form.is_valid():
            row = form.cleaned_data['row']
            column = form.cleaned_data['column']
            value = form.cleaned_data['value']
            agg_func = form.cleaned_data['agg_func']
            # get records from db based on query
            queryset = None
            df = pd.DataFrame.from_records(queryset)
            # create pivot table
            pivot_table = pd.pivot_table(df, values=value, index=row, columns=column, aggfunc=agg_func)
            # transform to the html
            pivot_table = pivot_table.to_html()
    else:
        form = PivotTableForm()
    context = {
        'form': form,
        'pivot_table': pivot_table
    }
    return render(request, 'pivot_table.html', context)