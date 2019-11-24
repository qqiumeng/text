from django import forms
from medicine.models import *

class add(forms.ModelForm):

    class Meta:
        model=Drug
        fields=['drug_num','drug_img','purchasing_price','selling_price','drug_name','drug_type','brief_description','expiration_time','detail','manufacturer','taking_instructions','remark','state','surplus']

