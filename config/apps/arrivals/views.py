# config/apps/arrivals/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..accounts.models import Profile  # accounts 앱의 Profile 모델 임포트
from .forms import StationSearchForm
from .services import fetch_realtime_arrivals_by_station


def index(request):
    """
    메인 페이지 뷰. 지하철역 검색 폼과 로그인한 사용자의 선호역을 표시합니다.
    """
    form = StationSearchForm(request.GET or None)
    station_name = None
    arrivals_data = None
    preferred_stations = []

    if request.user.is_authenticated:
        # 로그인한 사용자의 프로필에서 선호역을 가져옵니다.
        profile, _ = Profile.objects.get_or_create(user=request.user)
        preferred_stations = [
            station for station in [profile.preferred_station_1, profile.preferred_station_2, profile.preferred_station_3] if station
        ]

    if form.is_valid():
        station_name = form.cleaned_data["station"]
        arrivals_data = fetch_realtime_arrivals_by_station(station_name)

    context = {"form": form, "station_name": station_name, "arrivals_data": arrivals_data, "preferred_stations": preferred_stations}
    return render(request, "arrivals/index.html", context)