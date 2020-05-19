from django.conf.urls import url,re_path
from django.urls import path
from . import views


urlpatterns = [
    url(r'addSite/', views.addSite),
    url(r'addExam/', views.addExam),
    re_path(r'upload/(?P<examId>[0-9]+)$', views.upload, name = 'upload'),
    re_path(r'^download/(?P<fileId>[0-9]+)/$', views.download, name = 'download'),
    #url(r'^getExamList/?P<pageIndex>(\d+)/$', views.getExamList),
    re_path(r'^getExamList/(?P<pageIndex>[0-9]*)/$', views.getExamList),
    #path('setPrintService/<examId>', views.setPrintService),
    re_path(r'^setPrintService/(?P<examId>[0-9]+)/$', views.setPrintService, name = 'setPrintService'), 
    re_path(r'^savePrintTemplate/(?P<examId>[0-9]+)/$', views.savePrintTemplate, name = 'savePrintTemplate'), 
    url(r'4', views.addExamResult, name = 'add-exam-result'),
    url(r'5', views.addSiteResult, name = 'add-site-result'),
]