from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        post_form.save()
        return redirect('/')
    else:
        post_form = PostForm()
    return render(request, 'post_create.html', {'post_form': post_form})



