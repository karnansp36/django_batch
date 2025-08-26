from django.shortcuts import render
from .forms import BlogForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Blog
@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return HttpResponse("Post created successfully")
        else:
            return HttpResponse("Post not created")
    return render(request, 'create_post.html', {"form": BlogForm()})

def profile_post_list(request):
    posts = Blog.objects.filter(author=request.user)
    return render(request, 'profile_posts.html', {"posts": posts})

def update_post(request, post_id):
    post = Blog.objects.get(id=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse("Post updated successfully")
        else:
            return HttpResponse("Post not updated")
    return render(request, 'update_post.html', {"form": BlogForm(instance=post)})


def delete_post(request, post_id):
    post = Blog.objects.get(id=post_id)
    post.delete()
    return HttpResponse("Post deleted successfully")