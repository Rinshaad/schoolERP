from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'teacher/home.html')

def profile(request):
    return render(request,'teacher/profile.html')

def add_attendence(request):
    return render(request,'teacher/add_attendence.html')

def view_student(request):
    return render(request,'teacher/view_student.html')
