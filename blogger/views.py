from django.shortcuts import render
import requests
from .models import Post, PostForm, Comment, CommentForm
from django.utils import timezone
from django.core.paginator import Paginator

def post_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #p = Paginator(posts, 7)
    #page = request.GET.get('page')
    #p_post = p.page(page)
    return render(request, 'blogger/post_list.html', {'posts': posts, 'form': form})

def post_comments(request, post_id):
    post = Post.objects.filter(pk = post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.author = request.user
            comm.post = post_id
            comm.published_date = timezone.now()
            comm.save()
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post=post_id, published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blogger/post_comments.html', {'post': post, 'comments': comments, 'form': form})



