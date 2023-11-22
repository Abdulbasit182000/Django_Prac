from django import forms
from .models import Author, Book, Publisher


class PublisherModelForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [
            "name",
            "address",
            "city",
            "state_province",
            "country",
            "website",
        ]


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "salutation",
            "name",
            "email",
        ]


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "publisher",
            "publication_date",
        ]
