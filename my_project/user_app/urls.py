from django.urls import path
from .views import home, login_view, base_signup, logout_view
urlpatterns = [
    path('signup/', base_signup, name='base_signup'),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    ]