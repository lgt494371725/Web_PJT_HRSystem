from django import forms
from .models import TPreCareer


class PreCareerCreateForm(forms.ModelForm):

    class Meta:
        model = TPreCareer
        fields = ('role', 'start_date', 'end_date', 'exp_detail')
