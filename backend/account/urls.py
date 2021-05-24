from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('getUser/', views.getUser, name='getUser'),
    path('getUserAll/', views.getUserAll, name='getUserAll'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),
    path('updateUser/', views.updateUser, name='updateUser'),
]
