from django.shortcuts import render


def home(request):
    return render(request, 'blog/homepage.html')


def materials(request):
    return render(request, 'blog/materials.html')
