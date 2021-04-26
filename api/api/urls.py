"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import ItemViewSet, SoldItemViewSet, CommentViewSet

item_list = ItemViewSet.as_view({ 'get':'list' })
item_detail = ItemViewSet.as_view({ 'get':'retrieve' })
soliditem_list = SoldItemViewSet.as_view({ 'get':'list' })
solditem_detail = SoldItemViewSet.as_view({ 'get':'retrieve' })
comment_list = CommentViewSet.as_view({ 'get':'list' })
comment_detail = CommentViewSet.as_view({ 'get':'retrieve' })

urlpatterns = [
    path('admin/', admin.site.urls),
    #api/posts
    path('apiitem/', item_list, name='item_list'),
    #api/posts/int
    path('apiitem/<int:pk>', item_detail, name='item_detail'),
    #api/posts
    path('apisolditem/', soliditem_list, name='soliditem_list'),
    #api/posts/int
    path('apisolditem/<int:pk>', solditem_detail, name='solditem_detail'),
    #api/posts
    path('apicomment/', comment_list, name='comment_list'),
    #api/posts/int
    path('apicomment/<int:pk>', comment_detail, name='comment_detail'),
]
