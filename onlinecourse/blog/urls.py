from django.urls import path
from . import views

urlpatterns = [
    # homepage
    path('', views.home, name='home'),

    # courses
    path('courses/', views.courses, name='courses'),
    path('course/<int:id>', views.course, name='onecourse'),
    path('add_course/', views.add_course, name='add_course'),

    # materials
    path('materials/', views.materials, name='materials'),

    # user
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
