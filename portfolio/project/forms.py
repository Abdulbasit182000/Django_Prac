from django import forms
from .models import Author


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=[
            'salutation',
            'name',
            'email',
        ]