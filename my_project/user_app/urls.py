from django.urls import path
from .views import home, login_view, base_signup, logout_view
from .post import create_post, profile_post_list, update_post, delete_post
urlpatterns = [
    path('signup/', base_signup, name='base_signup'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('create_post/', create_post, name='create_post'),
    path('profile_posts/', profile_post_list, name='profile_posts'),
    path('update_post/<int:post_id>/', update_post, name='update_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    ]