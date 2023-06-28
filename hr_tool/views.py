from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import pandas as pd
from .forms import PivotTableForm

# pivot table analysis page
def analysis(request):
    if request.method == 'POST':
        form = PivotTableForm(request.POST)
        if form.is_valid():
            row = form.cleaned_data['row']
            column = form.cleaned_data['column']
            value = form.cleaned_data['value']

            # get records from db based on query
            queryset = None
            df = pd.DataFrame.from_records(queryset)

            # create pivot table
            pivot_table = pd.pivot_table(df, values=value, index=row, columns=column)

            # transform to the 
            html = pivot_table.to_html()
            return HttpResponse(html)
    else:
        form = PivotTableForm()
    return render(request, 'hr_tool/pivot_table.html', {'form': form})