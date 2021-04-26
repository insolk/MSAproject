from rest_framework import serializers
from .models import Comment, Item, SoldItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'item_no',
            'user_no', 
            'item_title', 
            'item_views',
            'item_price',
            'item_detail',
            'item_img',
            'item_status',
            'item_soldtime',
            'item_date',
        ]

class SoldItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldItem
        fields = [
            'item_no',
            'user_no',
            'item_title',
            'item_views',
            'item_price',
            'item_detail',
            'item_soldtime',
        ]



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'comment_no',
            'item_no',
            'comment_modify_date',
            'comment_create_date',
            'comment_content',
            'comment_nickname',
        ]
