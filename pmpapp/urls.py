from django.urls import path

from . import views

app_name = 'pmp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name="user_login")
]
