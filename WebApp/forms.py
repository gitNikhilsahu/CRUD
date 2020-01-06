from .models import Company
from django import forms

class NewForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'company_logo',
            'company_city',
        ]