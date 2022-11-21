from django.urls import path

from .import views

app_name='index'

urlpatterns = [
    
    path('',views.home,name='index'),
    path('studentlogin',views.studentlogin,name='student_login'),
    path('adminlogin',views.adminlogin,name='admin_login'),
    path('teacherlogin',views.teacherlogin,name='teacher_login'),
    path('master',views.master)
]
