from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Name'}), required=True,max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Father's name"}),required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'inputPassword6', 'placeholder': "Mother's name"}),required=True, max_length=50)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Email'}), required=True,max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

