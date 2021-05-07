from django.forms import ModelForm
from .models import Books, BookComments
from django import forms

class CreateBookForm(forms.ModelForm):

    title = forms.CharField(label="Title", required=True)
    author = forms.CharField(label="Author", required=True)
    location = forms.CharField(label="Location", required=False)
    is_digital = forms.BooleanField(required=False)

    class Meta:
        model = Books
        fields = ('book_image', 'title', 'author', 'location', 'is_digital')


class EditBookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('book_image', 'title', 'author', 'location', 'is_digital')
