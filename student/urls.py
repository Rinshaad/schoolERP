from django.urls import path

from .import views

app_name='student'

urlpatterns = [
    
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('attendence',views.view_attendence,name='attendence'),
    path('password',views.change_password,name='password'),
    
]
