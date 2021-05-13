from django.forms import ModelForm
from .models import Books, BookComments, BookCheckout
from django.core.exceptions import ValidationError
from django import forms

class CreateBookForm(forms.ModelForm):

    title = forms.CharField(label="Title", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label="Author", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label="Location", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_digital = forms.BooleanField(required=False)

    class Meta:
        model = Books
        fields = ('book_image', 'title', 'author', 'location', 'is_digital')


        def clean_is_digital(self):
            
            is_digital = self.cleaned_data.get('is_digital', '') == 'on'
            if is_digital != None:
                location = self.cleaned_data.get('location')
                if location == None:
                    raise ValidationError('Location field is required')
                return self.location

            # is_digital = self.cleaned_data.get("is_digital")
            # if is_digital == None:
            #     raise forms.ValidationError("Please input the location of the book.")
            # else:
            #     return is_digital


class EditBookForm(forms.ModelForm):

    title = forms.CharField(label="Title", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label="Author", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label="Location", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Books
        fields = ('book_image', 'title', 'author', 'location', 'is_digital')
    

class AddComment(forms.ModelForm):

    comment = forms.CharField(label="Comment", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = BookComments
        fields = ('comment',)


# class Checkout(forms.ModelForm):

#     class Meta:
#         model = BookCheckout
#         fields = ()