from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('getUserAll/', views.getUserAll, name='getUserAll'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),
]
