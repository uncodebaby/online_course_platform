from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from ..forms import CourseForm
from ..models import Course


@login_required(login_url='login')
def courses(request):
    all_courses = Course.objects.all()
    paginator = Paginator(all_courses, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/courses.html', context={'page_obj': page_obj})


def course_info(request, id):
    course = Course.objects.get(pk=id)
    return render(request, 'blog/course.html', context={'course': course})


@login_required(login_url='login')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.save()
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'blog/add_course.html', {'form': form})
