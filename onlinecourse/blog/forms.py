from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Course
from django.contrib.auth.models import User


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
