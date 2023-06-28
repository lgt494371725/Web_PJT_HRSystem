from django import forms
from .models import *


class PivotTableForm(forms.Form):
    row = forms.ModelChoiceField(queryset=MyData.objects.all())
    column = forms.ModelChoiceField(queryset=MyData.objects.all())
    value = forms.ModelChoiceField(queryset=MyData.objects.all())