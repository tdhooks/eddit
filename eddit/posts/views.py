from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from datetime import datetime

from .models import Post, Comment

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:25]
    context = {'latest_posts': latest_posts}
    return render(request, 'posts/index.html', context)

def focus(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    latest_comments = Comment.objects.filter(post = post_id).order_by('-pub_date')[:25]
    context = {'post': post, 'latest_comments': latest_comments}
    return render(request, 'posts/post_focus.html', context)

def post(request):
    if request.method == 'POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        pub_date = datetime.now()
        Post.objects.create(title=title, content=content, pub_date=pub_date)
        return redirect(index)
    else:
        return render(request, 'posts/post_form.html')

def comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content', None)
        pub_date = datetime.now()
        Comment.objects.create(post_id=post_id, content=content, pub_date=pub_date)
        return redirect(focus, post_id=post_id)
    else:
        post = get_object_or_404(Post, pk = post_id)
        context = {'post': post}
        return render(request, 'posts/comment_form.html', context)