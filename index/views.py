from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,('index/home.html'))
def adminlogin(request):
    return render(request,('index/admin_login.html'))
def studentlogin(request):
    return render(request,('index/student_login.html'))
def teacherlogin(request):
    return render(request,('index/teacher_login.html'))
def master(request):
    return render(request,('index/master.html'))
