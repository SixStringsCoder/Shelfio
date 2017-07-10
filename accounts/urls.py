from django.conf.urls import url
from .views import register, login, profile, reset_pw
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'register/', register, name='register'),
    url(r'login/', login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': '/'}, name='logout'),
    url(r'profile/', profile, name='profile'),
    url(r'reset_profile/', reset_pw, name='change_password')   # Handles POST Only
]
