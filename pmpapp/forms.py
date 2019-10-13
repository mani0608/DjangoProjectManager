from django import forms
from pmpapp.models import UserInfo, ProjectInfo
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class RegisterForm(forms.ModelForm):

    class Meta():
        model = UserInfo
        fields = ('website', 'profile_picture')


class ProjectForm(forms.ModelForm):

    class Meta():
        model = ProjectInfo
        fields = ('name', 'duration', 'start_date',
                  'project_model', 'current_resource_count')
