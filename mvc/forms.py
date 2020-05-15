from django.forms import ModelForm
from django import forms
from mvc.models import *

class SiteForm(ModelForm):
    class Meta:
        model = ExamSite
        fields = '__all__'

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class UploadForm(forms.Form):
    file = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple': True}), label = '选择文件...', help_text = '最大100M')

class ATForm(ModelForm):
    class Meta:
        model = ATSetInfo
        fields = ('beginTime', 'endTime', 'content', 'state')

class INForm(ModelForm):
    class Meta:
        model = INSetInfo
        fields = ('checkInTime', 'drawTime', 'deadlineTime', 'startIVTime', 'beginTime', 'endTime', 'content', 'state')