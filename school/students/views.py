from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, "students.html", {"allstudents":students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        standard = request.POST.get('standard')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        student = Student(
            name = name,
            standard = standard,
            contact = contact,
            email = email,
            image = image if image else None
        )
        student.save()
        return redirect("all-students")
    return render(request, "students.html")

def update_student(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        standard = request.POST.get('standard')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        student = Student(
            id = id,
            name = name,
            standard = standard,
            contact = contact,
            email = email,
            image = image if image else None
        )
        student.save()
        return redirect("all-students")
    return render(request, 'students.html',{'student': student} )

def delete_student(request, id):
    student = Student.objects.filter(id=id)
    student.delete()

    return redirect("all-students")