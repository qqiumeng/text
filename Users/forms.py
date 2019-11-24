from django import forms
from Role.models import *


class UserInfo(forms.ModelForm):
    class Meta:
        model = ManageUsers
        fields = ['login_name','password']
