from django.urls import path
from .views import SigninView
# from .views import SignupView, SigninView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from . import views

urlpatterns = [
    # path('signin', views.index, name='index'),
    # path('signin', SigninView.as_view()),
    # path('signin', SigninView.as_view()),
    # path('api-token-auth/', obtain_jwt_token)
]