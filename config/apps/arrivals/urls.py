from django.urls import path
from . import views

app_name = "arrivals"  # 이 앱의 URL에 대한 네임스페이스

urlpatterns = [
    path("", views.index, name="index"),  # 메인 페이지 (예: http://127.0.0.1:8000/)
]