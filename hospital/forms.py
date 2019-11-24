from django import forms
from ckeditor.widgets import CKEditorWidget
from hospital.models import Patient


class HospitalForm(forms.Form):
    # medical_record_No = forms.IntegerField(label='病历号')
    nurse = forms.CharField(label='护理')
    bed_num = forms.IntegerField(label='床号')
    cash = forms.IntegerField(label='押金')
    illness = forms.CharField(label='病情', widget=CKEditorWidget(config_name='illnes_ckeditor'),error_messages={'required': '病情不能为空'})

