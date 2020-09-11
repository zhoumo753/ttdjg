from django.db import models
from django.contrib import admin
from django import forms

# Create your models here.
# @admin.register(Grades)

class Grades(models.Model):
    gname = models.CharField(max_length=20,verbose_name='班级名')
    gdate = models.DateTimeField(verbose_name='时间')
    ggirlnum = models.IntegerField(verbose_name='女生数量')
    gboynum = models.IntegerField(verbose_name='男生数量')
    isDelete = models.BooleanField(default=False,verbose_name='删除')

    class Meta:
        verbose_name = "班级"
        verbose_name_plural = '班级'

class StudentsManager(models.Manager):

    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)

    def createStudent(cls, name, age, gender, contend,grade,isD=False):
        stu = self.model()
        # print(type(grade))
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        return stu

class Students(models.Model):
    sname = models.CharField(max_length=20,verbose_name='姓名')
    sgender = models.BooleanField(default=True,verbose_name='性别')
    sage = models.IntegerField(verbose_name='年龄')
    scontend = models.CharField(max_length=20,verbose_name='座右铭')
    isDelete = models.BooleanField(default=False,verbose_name='删除')
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE,verbose_name='班级名')

    stuObj = models.Manager()
    stuObj2 = StudentsManager()

    def createStudent(cls, name, age, gender, contend,grade,isD=False):
        stu = cls(sname=name, sage=age, sgender=gender,scontend=contend, sgrade=grade,isDelete=isD)
        return stu

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = '学生'
    
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):

    inlines = [StudentsInfo]

    def agpk(self):
        return self.id
    agpk.short_description = "序号"
            
    list_display = [agpk, 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete'] # 显示字段设置
    list_filter = ['gname'] # 过滤字段设置
    search_fields = ['gname'] # 搜索字段设置
    list_per_page = 10 # 分页设置
    # 添加，修改页属性
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']
    # fieldsets = [
    #     ("num",{"fields":['ggirlnum', 'gboynum']}),
    #     ("base", {"fields":["gname", "gdate", "isDelete"]}),
    # ] 
    # 规定属性的先后顺序
    # fieldsets = [] # 给属性分组 注意：fields与fieldsets不能同时使用

    ordering = ['id']# 按订单升序排列 不需要再meta里面处理
    # class Meta:
    #     db_table = "my_app_grades"
    #     ordering = ['-id']# 按订单升序排列

class StudentsAdmin(admin.ModelAdmin):
    
    def pk(self):
        return self.id
    pk.short_description = "序号"

    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    list_display = [pk, 'sname', 'sgender', 'sage','scontend', 'isDelete'] # 显示字段设置
    list_filter = ['sname'] # 过滤字段设置
    list_per_page = 20 # 分页设置
    
    # search_fields = [] # 搜索字段设置
    # list_per_page = [] # 分页设置
    # # 添加，修改页属性
    # fields = [] # 规定属性的先后顺序
    # fieldsets = [] # 给属性分组 注意：fields与fieldsets不能同时使用
    
    actions_on_top = False
    actions_on_bottom = True 

    ordering = ['id']# 按订单升序排列 不需要再meta里面处理


class Scores(models.Model):

    name = models.CharField(max_length=20,default='',verbose_name='姓名')
    yuwen = models.IntegerField(verbose_name='语文')
    shuxue = models.IntegerField(verbose_name='数学')
    yingyue = models.IntegerField(verbose_name='英语')

    isDelete = models.BooleanField(default=False,verbose_name='删除')

    class Meta:
        verbose_name = "成绩"
        verbose_name_plural = '成绩'

class ScoresAdmin(admin.ModelAdmin):

    def pk(self):
        return self.id
    pk.short_description = "序号"

    list_display = [pk,'name','yuwen','shuxue','yingyue','isDelete'] # 显示字段设置
    # list_display = ['pk','name','yuwen','isDelete']
    list_filter = ['name','yuwen'] # 过滤字段设置
    list_per_page = 20 # 分页设置
    
#     search_fields = ['name'] # 搜索字段设置
#     # list_per_page = [] # 分页设置
#     # # 添加，修改页属性
#     # fields = [] # 规定属性的先后顺序
#     # fieldsets = [] # 给属性分组 注意：fields与fieldsets不能同时使用
    
#     actions_on_top = False
#     actions_on_bottom = True 

    ordering = ['id']# 按订单升序排列 不需要再meta里面处理






    

    
    



