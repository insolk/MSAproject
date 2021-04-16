from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render,get_object_or_404, redirect
from items.models import Item, Comment
from django.contrib.auth.models import User
from items.forms import CommentForm, UDForm
from django.utils import timezone

# Create your views here.

def item_detail(request, pk):
    item_id = 1
    #product= Item.objects.filter(item_id= item_id)

    product = get_object_or_404(Item, item_id= item_id)
    comment= Comment.objects.filter(item_id= item_id).order_by('-create_date')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #comment.author = request.user 로그인 하게 되면 
            comment.create_date = timezone.now()
            print('여기')
            comment.item = product
            comment.save()
            return redirect('items:item_detail',1)#, 제목)
    else:
        form = CommentForm()
    
    paginator = Paginator(comment, 4)
    page_no = request.GET.get('page')
    try:
        comments = paginator.page(page_no)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render(request, 'items/item_detail.html', {'product':product,'comment': comments } )


def comment_detail(request, pk):
    comment = get_object_or_404(Comment, comment_id= pk)
    
    if request.method == "POST":
        UDform = UDForm(request.POST)
        if UDform.is_valid():
            if UDform.cleaned_data['UD'] == 'update':
                return render(request, 'items/comment_detail.html')
            
            elif UDform.cleaned_data['UD'] == 'delete':
                Comment.objects.filter(comment_id=pk).delete()
    return render(request, 'items/comment_detail.html', {'comment':comment} )



