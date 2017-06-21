from django import forms
from django.contrib.auth.models import User

class SearchForm(forms.ModelForm):
    query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
    )

    class Meta:
        model = User
        exclude = []
        fields = []

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
