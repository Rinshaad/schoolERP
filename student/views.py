from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'student/home.html')

def profile(request):
    return render(request,'student/profile.html')

def change_password(request):
    return render(request,'student/change_password.html')

def view_attendence(request):
    return render(request,'student/view_attendence.html')
