from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'addSite', views.addSite),
    url(r'addExam', views.addExam),
    url(r'', views.addExamResult, name = 'add-exam-result'),
    url(r'', views.addSiteResult, name = 'add-site-result'),
]