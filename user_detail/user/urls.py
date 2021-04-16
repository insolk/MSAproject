from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('<int:pk>', userDV.as_view(), name='user_detail'),
]