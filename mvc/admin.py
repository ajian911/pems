from django.contrib import admin
from mvc.models import ATSetInfo,INSetInfo,testModel

# Register your models here.
admin.site.register(ATSetInfo)
admin.site.register(INSetInfo)
admin.site.register(testModel)