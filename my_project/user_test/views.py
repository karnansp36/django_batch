from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse, Http404
from django.contrib import messages
from .forms import UserForm, ImageForm
from .models import User_db, image_storage
from django.views.decorators.clickjacking import xframe_options_exempt


def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully")
        else:
            messages.error(request, "Error in form submission")
    else:
        form = UserForm()
    return render(request, 'user_db.html', {"form": form})


def image_create_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded successfully")
        else:
            messages.error(request, "Error in image upload")
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {"form": form})


def user_list_view(request):
    images = image_storage.objects.all()
    return render(request, 'insta_post.html', {"images": images})


@xframe_options_exempt
def view_pdf(request, pk):
    obj = get_object_or_404(image_storage, pk=pk)
    if not obj.files:
        raise Http404("No file found")

    response = FileResponse(open(obj.files.path, "rb"), content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="%s"' % obj.files.name
    return response