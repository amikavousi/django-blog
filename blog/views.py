from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    data = {
        'title': 'all',
        'posts': Post.objects.all()
    }
    return render(request, 'index.html', context=data)


def show(request, id):
    post = Post.objects.get(id=id)
    data = {
        'title': post.title,
        'post': post
    }
    return render(request, 'show.html', context=data)


def author_show(request, user_id):
    posts = Post.objects.filter(author_id=user_id)
    data = {
        'title': posts.first().author,
        'posts': posts
    }
    return render(request, 'index.html', context=data)
