from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from . import views
urlpatterns = [
    #localhost/signup
    path('signup/', views.index, name='index'), #회원가입 페이지
    #localhost/signup/check
    path('signup/check', views.signup, name='success'), #회원가입 성공 후 페이지
    #localhost/signup/list 
    path('signup/list', views.get) #회원가입된 사용자 목록
                                    #추후 삭제할 기능
]