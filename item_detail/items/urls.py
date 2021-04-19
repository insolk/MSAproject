from django.contrib import admin
from django.urls import path, include
from . import views

app_name='items'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/<int:product_id>/', views.item_detail, name='items_detail'),
    path('items/<int:product_id>/comment', views.comment_insert, name='comment_insert'),
    path('items/<int:product_id>/comment/<int:comment_id>', views.comment_detail, name='comment_detail'),
    path('items/<int:product_id>/comment/<int:comment_id>/update',views.comment_update, name='comment_update')
]
