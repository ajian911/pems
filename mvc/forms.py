from django.forms import ModelForm
from django import forms
from mvc.models import *
#from tinymce.widgets import TinyMCE

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
    #content = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 10}))
    class Meta:
        model = ATSetInfo
        fields = ('beginTime', 'endTime', 'content', 'state')

class INForm(ModelForm):
    #content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = INSetInfo
        fields = ('checkInTime', 'drawTime', 'deadlineTime', 'startIVTime', 'beginTime', 'endTime', 'content', 'state')