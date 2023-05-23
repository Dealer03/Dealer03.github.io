from django.contrib import admin
from .models import UserRequest, UserLogin

# Register your models here.
admin.site.register(UserLogin)
admin.site.register(UserRequest)
