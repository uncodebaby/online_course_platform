from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import CourseForm, CreateUserForm
from .models import Course
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'blog/homepage.html')


@login_required(login_url='login')
def courses(request):
    all_courses = Course.objects.all()
    paginator = Paginator(all_courses, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/courses.html', context={'page_obj': page_obj})


def materials(request):
    return render(request, 'blog/materials.html')


def course(request, id):
    course = Course.objects.get(pk=id)
    return render(request, 'blog/course.html', context={'course': course})


@login_required(login_url='login')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'blog/add_course.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            messages.error(request, 'Uncorrected data')
    else:
        form = CreateUserForm()
    return render(request, 'blog/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect.')
            return render(request, 'blog/login.html')
    return render(request, 'blog/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
