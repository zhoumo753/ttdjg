from django.urls import path,include
from . import views
 
urlpatterns = [
     path('grades/',views.grades),
     path('students/',views.students),
    
     path('geturl1',views.geturl1),

     path('showregister/', views.showregist),
     path('showregister/register/', views.regist),
     path('redirect1/', views.redirect1),
     path('redirect2/', views.redirect2),

     path('showmain/',views.showmain),
     path('main/',views.main),
     path('login/',views.login),
     path('quit/',views.quit),

     path('',views.index),
]