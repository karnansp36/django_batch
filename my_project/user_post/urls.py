from django.urls import path
from .views import create_post, post_list, post_only

urlpatterns = [
    path('create/', create_post),
    path('list/',post_list ),
    path('list/details/<int:post_id>',post_only ),
]