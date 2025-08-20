from django.urls import path
from .views import user_create_view, image_create_view, user_list_view

urlpatterns = [
    path('create/', user_create_view, name='user_create'),
    path('image_upload/', image_create_view, name='image_upload'),
    path('explore/', user_list_view, name='user_list'),
]