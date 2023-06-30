from django import forms
from .models import TPreCareer
from .models import TAssignExp
from .models import TProject

class PreCareerCreateForm(forms.ModelForm):

    class Meta:
        model = TPreCareer
        fields = ('role', 'start_date', 'end_date', 'exp_detail')
        

class AssignExpCreateForm(forms.ModelForm):

    class Meta:
        model = TAssignExp
        fields = ('role', 'start_date', 'end_date','project')

    def __init__(self, *args, **kwargs):
        super(AssignExpCreateForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = TProject.objects.all()
