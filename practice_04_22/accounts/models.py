from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User 모델을 정의
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profiles/')


