from django.db import models
from django.utils import timezone

# Create your models here.
#考试类别
TYPE_CHOICES = (
    ("公务员考录" , "公务员考录"),
    ("事业招聘" , "事业招聘"), 
    ("专业技术资格" , "专业技术资格"),
    ("社会化考试" , "社会化考试"),
)
#考试形式
METHOD_CHOICES = (
    ("面试" , "面试"),
    ("笔试" , "笔试"), 
    ("机考" , "机考"),
)

class Exam(models.Model):  #考试模型类
    name = models.CharField('考试名称', max_length = 100)
    date = models.DateField('考试日期')
    siteName = models.CharField('考点名称', max_length = 100, blank = True)
    adress = models.CharField('考点地址', max_length = 100, blank = True)
    examineeNum = models.IntegerField('考生人数', blank = True)
    examType = models.CharField('考试类别', max_length = 20, choices = TYPE_CHOICES, default = TYPE_CHOICES[3])
    examMethod = models.CharField('考试形式', max_length = 20, choices = METHOD_CHOICES, default = METHOD_CHOICES[1])
    remarks = models.TextField('备注', max_length = 500, blank = True)

class Examinee(models.Model): #考生模型类
    name = models.CharField('考生姓名', max_length = 20)
    IDNumber = models.CharField('身份证号', max_length = 18)
    ATID = models.CharField('准考证号', max_length = 11)


class AdmissionTicket(models.Model): #笔试准考证模型
    examID = models.CharField("关联考试", max_length = 20) 
    name = models.CharField("考生姓名", max_length = 20)  
    IDNumber = models.CharField("身份证号", max_length = 18)
    ATID = models.CharField("准考证号", max_length = 11)
    applyUnit = models.CharField("报考单位", max_length = 100, blank = True, null = True)
    applyPosition = models.CharField("报考职位", max_length = 100, blank = True, null = True)
    phone = models.CharField("手机号码", max_length = 11, blank = True, null = True)
    date = models.CharField('考试日期',  max_length = 100, blank = True, null = True)
    siteName = models.CharField('考点名称', max_length = 100, blank = True, null = True)
    address = models.CharField('考点地址', max_length = 100, blank = True, null = True)
    subjectName = models.CharField('考试科目', max_length = 100, blank = True, null = True)
    subjectTime = models.CharField('科目时间', max_length = 100, blank = True, null = True)
    beginTime = models.DateTimeField("开始打印时间", auto_now = False, auto_now_add = False, null = True)
    endTime = models.DateTimeField("结束打印时间", auto_now = False, auto_now_add = False, null = True)
    ifQuery = models.BooleanField("是否已查询", default = '0') #0未查询，1已查询
    ifPrint = models.BooleanField("是否已打印", default = '0') #0未打印，1已打印
    state = models.BooleanField("当前状态", default = '0') #0未启动，1启动中
    

class InterviewNotification(models.Model): #面试通知书模型
    examID = models.CharField("关联考试", max_length = 20) 
    name = models.CharField("考生姓名", max_length = 20)  
    IDNumber = models.CharField("身份证号", max_length = 18)
    ATID = models.CharField("准考证号", max_length = 11)
    applyUnit = models.CharField("报考单位", max_length = 100, blank = True, null = True)
    applyPosition = models.CharField("报考职位", max_length = 100, blank = True, null = True)
    phone = models.CharField("手机号码", max_length = 11, blank = True, null = True)
    date = models.CharField('考试日期',  max_length = 100, blank = True, null = True)
    checkInTime = models.CharField("报到时间", max_length = 20, blank = True, null = True)
    drawTime = models.CharField("抽签时间", max_length = 20, blank = True, null = True)
    deadlineTime = models.CharField("截止时间", max_length = 20, blank = True, null = True)
    stratIVTime = models.CharField("开始时间", max_length = 20, blank = True, null = True)
    siteName = models.CharField('考点名称', max_length = 100, blank = True, null = True)
    address = models.CharField('考点地址', max_length = 100, blank = True, null = True)
    beginTime = models.DateTimeField("开始打印时间", auto_now = False, auto_now_add = False, null = True)
    endTime = models.DateTimeField("结束打印时间", auto_now = False, auto_now_add = False, null = True) 
    ifQuery = models.BooleanField("是否已查询", default = '0')
    ifPrint = models.BooleanField("是否已打印", default = '0')
    state = models.BooleanField("当前状态", default = '0')

class ExamSite(models.Model):  #考点模型类
    name = models.CharField('考点名称', max_length = 100)
    address = models.CharField('考点地址', max_length = 100)
    roomNum = models.IntegerField('考场数')
    roomMaxNum = models.IntegerField('最大考场数')
    chiefName = models.CharField('主考', max_length = 20)
    chiefPhone = models.CharField('主考联系方式', max_length = 11)
    directorName = models.CharField('考务负责人', max_length = 20)
    directorPhone = models.CharField('考务联系方式', max_length = 11)
    ifStandardized = models.BooleanField('是否标准化考场')
    remarks = models.TextField('备注', max_length = 500)

class ExamPerson(models.Model): #考务人员模型类
    name = models.CharField('姓名', max_length = 20)
    workUnit = models.CharField('工作单位', max_length = 100)
    post = models.CharField('工作职务', max_length = 30) 
    phone = models.CharField('联系方式', max_length = 11)
    role = models.CharField('考务岗位', max_length = 20)
    ifTemporary = models.BooleanField('是否临聘人员') 
    grade = models.IntegerField('评分')
    remarks = models.TextField('备注', max_length = 500)
    
class ExamStuff(models.Model): #考务材料模型类
    name = models.CharField('材料名称', max_length = 20)
    amount = models.IntegerField('数量')
    stuffType = models.CharField('类别', max_length = 20) #消耗品|非消耗品
    remarks = models.TextField('备注', max_length = 500)

class FileInfo(models.Model):
    examId = models.CharField('关联考试ID', max_length = 20, blank=True)
    name = models.CharField('文件名', max_length = 50)
    size = models.DecimalField("文件大小", max_digits = 10, decimal_places = 0)
    path = models.CharField("文件路径", max_length = 200)
    time = models.DateTimeField("上传时间", default = timezone.now())