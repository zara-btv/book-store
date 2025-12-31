from django import forms
from Book.models import Books

class CreateBook(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
