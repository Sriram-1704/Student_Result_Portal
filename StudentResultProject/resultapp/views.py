from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Student, Result
from .forms import StudentForm, ResultForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully for {user.username}!')
            return redirect('resultapp:home') 
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'resultapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('resultapp:home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'resultapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('resultapp:login')

@login_required
def home(request):
    total = Student.objects.count()
    return render(request, 'resultapp/home.html', {'total_students': total})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'resultapp/student_list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('resultapp:student_list')
    else:
        form = StudentForm()
    return render(request, 'resultapp/add_student.html', {'form': form})

@login_required
def add_marks(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            marks = form.save(commit=False)
            marks.student = student
            marks.save()
            messages.success(request, 'Marks added successfully!')
            return redirect('resultapp:student_list')
    else:
        form = ResultForm()
    return render(request, 'resultapp/add_marks.html', {'form': form, 'student': student})

@login_required
def view_result(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    results = Result.objects.filter(student=student).select_related('subject')
    
    total_marks = results.aggregate(total=Sum('marks_obtained'))['total'] or 0

    total_max_marks = results.aggregate(max_total=Sum('max_marks'))['max_total'] or 0
    if total_max_marks > 0:
        percentage = (total_marks / total_max_marks) * 100
    else:
        percentage = 0

    context = {
        'student': student,
        'results': results,
        'total_marks': total_marks,
        'total_max_marks': total_max_marks,  # New variable
        'percentage': round(percentage, 2),
    }
    return render(request, 'resultapp/view_result.html', context)