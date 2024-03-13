from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'Students/student_list.html', {'students': students})

def student_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'Students/student_view.html', {'student': student})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_view', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'Students/student_edit.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_view', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'Students/student_edit.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')