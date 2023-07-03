from django import forms
from .models import TPreCareer
from .models import TSkill
from .models import User

class PreCareerCreateForm(forms.ModelForm):

    class Meta:
        model = TPreCareer
        fields = ('role', 'start_date', 'end_date', 'exp_detail')

class SkillCreateForm(forms.ModelForm):

    class Meta:
        model = TSkill
        fields = ('skill', 'updated_date')

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('career_level', 'homeoffice','dte')
