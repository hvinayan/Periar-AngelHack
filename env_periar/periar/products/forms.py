from django import forms
from django.contrib.auth.models import User
from .models import Product, Cart, Category

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['pname', 'pdisc', 'image', 'price']

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['cname', 'cdisc']
