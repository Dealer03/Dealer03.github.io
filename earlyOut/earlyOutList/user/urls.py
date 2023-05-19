from django.urls import path
from django.contrib.auth import views
from user import views

app_name = 'user'
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
]
