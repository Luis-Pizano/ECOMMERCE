from django import forms # type: ignore
from .models import Account

class RegistartionForm(forms.ModelForm):
    class Meta:
        model = Account
        fields =[ 'first_name', 'last_name', 'phone_number', 'email', 'password']