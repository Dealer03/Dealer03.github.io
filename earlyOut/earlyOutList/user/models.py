from django.db import models
from .forms import User
from django.utils.timezone import datetime


# Create your models here.


class UserRequest(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    vr_username = models.CharField(max_length=50)
    vr_password = models.CharField(max_length=100)
    shift_date_time = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=datetime.now)

    def __str__(self):
        return self.vr_username
