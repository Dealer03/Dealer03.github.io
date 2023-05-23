from django.db import models
from .forms import User
from django.utils.timezone import datetime

# Create your models here.


class UserLogin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class UserRequest(models.Model):
    request_id = models.ForeignKey(
        UserLogin, on_delete=models.PROTECT, default=None)
    vr_username = models.CharField(max_length=50)
    vr_password = models.CharField(max_length=100)
    shift_date_time = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.vr_username
