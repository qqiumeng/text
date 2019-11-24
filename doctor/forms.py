from django import forms
from doctor.models import *



class add(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["doctor_name","card_type","card_num","phone","tel","sex","age","birth","email","office","level","remark","in_data","d_number"]
