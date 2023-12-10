from django import forms
from .models import Receipt

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('store_name','date_of_purchase', 'item_list', 'total_amount')

        widgets = {
            'store_name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'date_of_purchase': forms.DateInput(attrs={
            'class': INPUT_CLASSES
            }),
            'item_list': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'total_amount': forms.NumberInput(attrs={
            'class': INPUT_CLASSES
            }),

            
        }


class EditReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('store_name','date_of_purchase', 'item_list', 'total_amount')

        widgets = {
            'store_name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'date_of_purchase': forms.DateInput(attrs={
            'class': INPUT_CLASSES
            }),
            'item_list': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'total_amount': forms.NumberInput(attrs={
            'class': INPUT_CLASSES
            }),
        }