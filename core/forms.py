from django import forms

from core.models import Supplier, Product, Brand, Category, Customer
# Formulario para Cliente
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['dni', 'first_name', 'last_name', 'address', 'gender', 'date_of_birth', 'phone', 'email', 'image', 'state']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección', 'rows': 2}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['description', 'state']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la marca'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'description', 'cost', 'price', 'stock', 'iva', 'expiration_date',
            'brand', 'supplier', 'categories', 'line', 'image', 'state'
        ]
        widgets = {
            'expiration_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'categories': forms.CheckboxSelectMultiple,
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields=['name','ruc','address','phone','state']


# Formulario para Categoria
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['description', 'state']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }