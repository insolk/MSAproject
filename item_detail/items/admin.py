from django.contrib import admin

from .models import Comment, Item


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id','item_name', 'item_views','item_location','item_sellorname','item_sellorid','item_date','item_price','item_detail','item_img','item_status','item_dealtime']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['item','comment_content', 'create_date','modify_date']



admin.site.register(Comment, CommentAdmin)
admin.site.register(Item, ItemAdmin)
