from django.contrib import admin

from .models import Grades, Students,GradesAdmin,StudentsAdmin,Scores,ScoresAdmin

# Register your models here.
admin.site.site_header = '后台管理' #登录界面的标题
admin.site.site_title = '后台管理'

admin.site.register(Grades,GradesAdmin)
admin.site.register(Students,StudentsAdmin)
admin.site.register(Scores,ScoresAdmin)


