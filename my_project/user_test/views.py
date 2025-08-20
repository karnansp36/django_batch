from django.shortcuts import render
from .forms import UserForm, ImageForm
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from .models import User_db, image_storage

def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
        else:
            HttpResponse("Form is not valid")
            messages.error(request, "Error in form submission")
    else:
        form = UserForm()
    return render(request , 'user_db.html',{"form":form})

def image_create_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded successfully")
        else:
            messages.error(request, "Error in image upload")

    return render(request, 'image_upload.html', {"form": ImageForm()})

def user_list_view(request):
    images = image_storage.objects.all()
    return render(request, 'insta_post.html',{"images":images})

