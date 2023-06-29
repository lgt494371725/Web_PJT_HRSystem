from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, MDte, MHomeoffice


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'birthday',
            'dte',
            'homeoffice',
            'password1',
            'password2'
        )


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['dte'].queryset = MDte.objects.all()
        self.fields['homeoffice'].queryset = MHomeoffice.objects.all()
