# Django 관리자(admin) 기능을 불러옵니다.
# 관리자 페이지에 모델을 등록하면 웹 인터페이스에서 CRUD(생성,조회,수정,삭제)가 가능해집니다.
from django.contrib import admin

# 같은 앱(models.py)에 정의된 Profile 모델을 불러옵니다.
from .models import Profile


# @admin.register(Profile)
# 데코레이터 방식으로 Profile 모델을 관리자에 등록합니다.
# (아래 ProfileAdmin 클래스를 자동으로 연결해줌)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display:
    # 관리자(admin) 목록 페이지에서 표시할 컬럼들을 지정합니다.
    # 튜플 형태로 필드명을 나열하면 각 레코드가 테이블 형태로 표시됩니다.
    # 여기서는 user(사용자), default_station(기본역)이 한 줄에 표시됩니다.
    list_display = ("user", "preferred_station_1", "preferred_station_2", "preferred_station_3")
