from django import forms
from .models import Owner, Patient


class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ["first_name", "last_name", "phone"]
