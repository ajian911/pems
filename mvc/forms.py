from django.forms import ModelForm
from mvc.models import *

class SiteForm(ModelForm):
    class Meta:
        model = examSite
        fields = '__all__'

class ExamForm(ModelForm):
    class Meta:
        model = exam
        fields = '__all__'