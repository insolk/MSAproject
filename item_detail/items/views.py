from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, get_object_or_404, redirect
from items.models import Item, Comment
from django.contrib.auth.models import User
from items.forms import CommentForm, UDForm
from django.utils import timezone


# Create your views here.

def item_detail(request, product_no):
    # product= Item.objects.filter(item_id= item_id)

    product = get_object_or_404(Item, item_no=product_no)
    comment = Comment.objects.filter(item_no=product_no).order_by('-comment_create_date')

    paginator = Paginator(comment, 4)
    page_no = request.GET.get('page')
    try:
        comments = paginator.page(page_no)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render(request, 'items/item_detail.html', {'product': product, 'comment': comments})


def comment_insert(request, product_no):
    # 댓글 등록
    product = get_object_or_404(Item, item_no=product_no)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.author = request.user 로그인 하게 되면
            comment.comment_create_date = timezone.now()
            comment.item_no = product
            comment.save()
            return redirect('items_detail', product_no)  # , 제목)

    return redirect('items_detail', product_no)  # , 제목)


def comment_detail(request, product_no, comment_no):
    comment = get_object_or_404(Comment, comment_no=comment_no)
    if request.method == "POST":
        UDform = UDForm(request.POST)
        if UDform.is_valid():
            if UDform.cleaned_data['UD'] == 'update':
                return render(request, 'items/comment_detail.html', {'comment': comment, 'product_no': product_no})

            elif UDform.cleaned_data['UD'] == 'delete':
                Comment.objects.filter(comment_no=comment_no).delete()

                return redirect('items_detail', product_no)  # , 제목)

    return render(request, 'items/item_detail.html', {'comment': comment})


def comment_update(request, product_no, comment_no):
    comment = get_object_or_404(Comment, comment_no=comment_no)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            # comment = form.save(commit=False)
            # comment.author = request.user 로그인 하게 되면
            # comment.create_date = timezone.now()
            # comment.item = product
            comment.comment_modify_date = timezone.now()
            comment.save()
            return redirect('items_detail', product_no)  # , 제목)
    else:
        form = CommentForm()

    return redirect('items_detail', product_no)