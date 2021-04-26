from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #localhost/"signup의 url"
    path('', include('signup.urls')), 
    #localhost/"signin의 url"
    # path('', include('signin.urls')),
    #localhost/"itemlist의 url"
    path('', include('itemlist.urls')),

    path('userapi/',include('userapi.urls',namespace = 'userapi')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
