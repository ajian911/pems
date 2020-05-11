from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'addSite', views.addSite),
    url(r'addExam', views.addExam),
    url(r'1', views.addExamResult, name = 'add-exam-result'),
    url(r'2', views.addSiteResult, name = 'add-site-result'),
]