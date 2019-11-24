from django import forms
from Resource.models import *


class Resource_form(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'
