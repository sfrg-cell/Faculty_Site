from django.shortcuts import render
from .models import Program, Department, HomePageText 


def home(request):
    content = HomePageText.objects.first()
    return render(request, "app/home.html", {"content": content})

def programs(request):
    programs = Program.objects.all()
    return render(request, "app/programs.html", {"programs" : programs})

def programs_details(request, id):
    program = Program.objects.get(id=id)
    return render(request, "app/programs_details.html", {"program" : program})

def departments(request):
    departments = Department.objects.all()
    return render(request, "app/departments.html", {"departments" : departments})

def departments_details(request, id):
    department = Department.objects.get(id=id)
    return render(request, "app/departments_details.html", {"department" : department})
