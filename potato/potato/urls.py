from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('signin/', admin.site.urls),
    path('users/', include('signup.urls')),
    # path('users/', include('signin.urls')),
    path('', include('itemlist.urls')), #itemlist app의 urls파일에 있는 경로
]
