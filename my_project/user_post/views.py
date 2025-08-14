from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import UserPost

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content =request.POST.get("content")
        if title =="" or content == "":
            return HttpResponse('field should not be empty')
        else:
            UserPost.objects.create(title=title, content=content)
            return HttpResponse("Successfully created")
    return render(request, 'createPost.html')

def post_list(request):
    posts = UserPost.objects.all()
    return render(request, 'post_list.html', {"posts":posts})

def post_only(request,post_id):
    post = UserPost.objects.get(id=post_id)
    return render(request, 'post_details.html', {"post":post})