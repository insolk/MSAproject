
from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls', namespace='user')),
    path('logout/', logout, name='logout')
]
