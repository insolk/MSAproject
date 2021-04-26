from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import ItemSerializer, SoldItemSerializer, CommentSerializer
from api.serializers import SearchItemSerializer, SearchSoldItemSerializer, SearchCommentSerializer
from .models import SearchItem, SearchSoldItem, SearchComment
from .models import Item, SoldItem, Comment

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SoldItemViewSet(viewsets.ModelViewSet):
    queryset = SoldItem.objects.all()
    serializer_class = SoldItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SearchItemViewSet(viewsets.ModelViewSet):
    queryset = SearchItem.objects.all()
    serializer_class = SearchItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SearchSoldItemViewSet(viewsets.ModelViewSet):
    queryset = SearchSoldItem.objects.all()
    serializer_class = SearchSoldItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SearchCommentViewSet(viewsets.ModelViewSet):
    queryset = SearchComment.objects.all()
    serializer_class = SearchCommentSerializer
    # permission_classes = [permissions.IsAuthenticated]
