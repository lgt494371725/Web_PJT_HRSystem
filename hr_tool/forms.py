from django import forms

class SearchForm(forms.Form):
    search  = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)