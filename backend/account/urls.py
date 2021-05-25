from django.urls import path

from . import views
# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('getUser/', views.getUser, name='getUser'),
    path('getUserAll/', views.getUserAll, name='getUserAll'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),
    path('updateUser/', views.updateUser, name='updateUser'),
    #token관련 api
    # path('api/token/', obtain_jwt_token),
    # path('api/token/verify/', verify_jwt_token),
    # path('api/token/refresh/', refresh_jwt_token),
]
