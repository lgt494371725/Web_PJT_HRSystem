from django import forms
from .models import TPreCareer
from .models import TSkill


class PreCareerCreateForm(forms.ModelForm):

    class Meta:
        model = TPreCareer
        fields = ('role', 'start_date', 'end_date', 'exp_detail')

class SkillCreateForm(forms.ModelForm):

    class Meta:
        model = TSkill
        fields = ('skill', 'updated_date')

