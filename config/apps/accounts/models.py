# config/apps/accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


# 1. 커스텀 User 모델 정의
class User(AbstractUser):
    """
    Django 기본 User를 확장한 모델.
    username, password, email 등 기존 필드에 더해 nickname을 추가합니다.
    """
    nickname = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.username


# 2. Profile 모델 정의
class Profile(models.Model):
    """
    각 사용자(User)와 1:1 관계로 연결되는 프로필 정보.
    사용자의 자주 이용하는 지하철역(default_station)을 저장합니다.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    preferred_station_1 = models.CharField(max_length=50, blank=True, null=True)
    preferred_station_2 = models.CharField(max_length=50, blank=True, null=True)
    preferred_station_3 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
