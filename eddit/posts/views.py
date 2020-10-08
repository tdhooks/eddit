from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Post, Comment

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:25]
    context = {'latest_posts': latest_posts}
    return render(request, 'posts/index.html', context)

def focus(request, post_id):
    post = Post.objects.get(pk = post_id)
    latest_comments = Comment.objects.filter(post = post_id).order_by('-pub_date')[:25]
    context = {'post': post, 'latest_comments': latest_comments}
    return render(request, 'posts/post_focus.html', context)
