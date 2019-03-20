from django.shortcuts import render, redirect
from .models import Post
# from .forms import PostForm


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')
