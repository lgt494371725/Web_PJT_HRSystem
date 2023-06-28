from django import forms
from .models import *


class PivotTableForm(forms.Form):
    CHOICES = [
        ('', '----'),
        ('birth_year', '誕生日(年)'),
        ('birth_month', '誕生日(月)'),
        ('birth_year_month', '誕生日(年月)'),
        ('career_level', 'career level'),
        ('home_office', 'home_office'),
        ('DTE', 'DTE'),
        ('skill', 'skill'),
        ('join_year', '入社日(年)'),
        ('join_month', '入社日(月)'),
        ('join_year_month', '入社日(年月)'),
        ('assign_role', 'assign role'),
        ('assign_experience', 'assign経験数'),
        ('assign_industry', 'assign industry'),
    ]
    AGG_CHOICES = [
        ('', '----'),
        ('min', 'min'),
        ('max', 'max'),
        ('mean', 'mean'),
        ('median', 'median'),
        ('sum', 'sum'),
        ('count', 'count'),
    ]
    row = forms.ChoiceField(choices=CHOICES)
    column = forms.ChoiceField(choices=CHOICES,required=False)
    value = forms.ChoiceField(choices=CHOICES)
    agg_func = forms.ChoiceField(choices=AGG_CHOICES)