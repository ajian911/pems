from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'addSite', views.addSite),
    url(r'addExam', views.addExam),
    #url(r'^getExamList/?P<pageIndex>(\d+)/$', views.getExamList),
    path('getExamList/<pageIndex>', views.getExamList),
    url(r'4', views.addExamResult, name = 'add-exam-result'),
    url(r'5', views.addSiteResult, name = 'add-site-result'),
]