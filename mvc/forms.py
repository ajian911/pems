from django.forms import ModelForm
from django import forms
from mvc.models import *
from tinymce.widgets import TinyMCE
from django.contrib.admin import widgets

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

class PTForm(ModelForm):
    #content = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 10}))
    #beginTime = forms.DateTimeField(required = True, label = '开始打印时间', widget = widgets.AdminSplitDateTime)
    #endTime = forms.DateTimeField(required = True, label = '结束打印时间', widget = widgets.AdminSplitDateTime)
    class Meta:
        model = printTemplate
        fields = ('beginTime','endTime','content','state','loginURL')

