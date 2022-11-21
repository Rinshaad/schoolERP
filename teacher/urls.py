from django.urls import path

from .import views
app_name='teacher'

urlpatterns = [
    
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('student',views.view_student,name='student'),
    path('attendence',views.add_attendence,name='attendence')
]
