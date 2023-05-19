from django.urls import path
from webDriver import views


urlpatterns = [
    path('webdriver', views.update_webdriver, name='webdriver'),
    path('automation', views.run_webdriver, name='automation'),
]
