from django.urls import path

from .import views

app_name='schooladmin'

urlpatterns = [
    path('home',views.home,name='home'),
    path('addstudent',views.view_student,name='viewstudent'),
    path('addstudent',views.add_student,name='addstudent'),
    path('attendence',views.view_attendence,name='viewattendence')
]
