import signin.views 
from . import views
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token\

urlpatterns = [
    #localhost:8000/signin
    path('signin/', views.index, name='index'), #로그인 화면
    #localhost:8000/signin/check
    path('signin/check', views.login, name='check') #로그인 후 화면 (메인으로 이동)
]