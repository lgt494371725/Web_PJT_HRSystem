from django import forms

class SearchForm(forms.Form):
    Search  = forms.CharField(required=False)
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)