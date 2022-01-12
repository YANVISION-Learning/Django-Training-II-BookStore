from django import forms

from book_app.models import BookOrder


class BookOrderForm(forms.ModelForm):
    class Meta:
        model = BookOrder
        fields = ['name', 'phone_number', 'message']
