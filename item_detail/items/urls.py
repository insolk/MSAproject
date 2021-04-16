from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'items'

urlpatterns = [
    #path('',views.item_detail, name='items_detail'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('<int:pk>/comment', views.comment_detail, name='comment_detail'),
    #path('<int:pk>/comment/delete', views.comment_update, name='comment_update')
]
