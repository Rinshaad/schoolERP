from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'schooladmin/home.html')

def add_student(request):
    return render(request,'schooladmin/add_student.html')

def view_attendence(request):
    return render(request,'schooladmin/view_attendence.html')

def view_student(request):
    return render(request,'schooladmin/view_student.html')

