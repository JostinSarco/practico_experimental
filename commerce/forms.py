from django import forms

from commerce.models import Invoice, Purchase, PurchaseDetail

class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields = ['customer', 'payment_method', 'issue_date', 'subtotal', 'iva', 'total']
        widgets = {
            'customer': forms.Select(),
            'payment_method': forms.Select(),
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'subtotal': forms.NumberInput(),
            'iva': forms.NumberInput(),
            'total': forms.NumberInput(),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['num_document', 'supplier', 'issue_date', 'subtotal', 'iva', 'total']
        widgets = {
            'num_document': forms.TextInput(),
            'supplier': forms.Select(),
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'subtotal': forms.NumberInput(),
            'iva': forms.NumberInput(),
            'total': forms.NumberInput(),
        }

class PurchaseDetailForm(forms.ModelForm):
    class Meta:
        model = PurchaseDetail
        fields = ['product', 'quantify', 'cost', 'subtotal', 'iva']
        widgets = {
            'product': forms.Select(),
            'quantify': forms.NumberInput(),
            'cost': forms.NumberInput(),
            'subtotal': forms.NumberInput(),
            'iva': forms.NumberInput(),
        }