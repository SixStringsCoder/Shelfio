from django.conf.urls import url
from .views import register, login, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'register/', register, name='register'),
    url(r'login/', login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': '/'}, name='logout'),
    url(r'profile/', profile, name='profile'),
]