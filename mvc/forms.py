from django.forms import ModelForm
from mvc.models import *

class SiteForm(ModelForm):
    class Meta:
        model = ExamSite
        fields = '__all__'

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'