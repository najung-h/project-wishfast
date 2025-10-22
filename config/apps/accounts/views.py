# Django의 단축 함수 render, redirect를 불러옵니다.
# render: 템플릿을 렌더링하여 HTML을 반환
# redirect: 다른 URL로 리다이렉트할 때 사용
from django.shortcuts import render, redirect

# 로그인된 사용자만 접근할 수 있도록 제한하는 데코레이터
# 비로그인 사용자가 접근하면 자동으로 로그인 페이지로 이동
from django.contrib.auth.decorators import login_required

# 같은 앱(forms.py)에서 ProfileForm을 불러옵니다.
# 사용자가 기본역을 입력/수정할 때 사용하는 폼
from .forms import ProfileForm

# 같은 앱(models.py)에서 Profile 모델을 불러옵니다.
# User 모델과 1:1로 연결되어 있으며, 기본역 정보를 저장함
from .models import Profile


# 로그인한 사용자만 접근할 수 있는 프로필 페이지 뷰 함수
@login_required
def profile_view(request):
    # 로그인한 사용자의 Profile 객체를 가져오거나, 없으면 새로 생성합니다.
    # get_or_create() → (객체, 생성여부) 튜플을 반환
    # prof: Profile 객체, _ : 새로 생성됐는지 여부(True/False)
    prof, _ = Profile.objects.get_or_create(user=request.user)

    # 사용자가 폼을 제출(POST 요청)했을 때
    if request.method == "POST":
        # 제출된 데이터를 기반으로 폼 인스턴스를 생성
        form = ProfileForm(request.POST)

        # 폼 데이터가 유효하면(cleaned_data에 접근 가능)
        if form.is_valid():
            # 입력받은 기본역(default_station)을 프로필에 반영
            prof.preferred_station_1 = form.cleaned_data["preferred_station_1"]
            prof.preferred_station_2 = form.cleaned_data["preferred_station_2"]
            prof.preferred_station_3 = form.cleaned_data["preferred_station_3"]

            # DB에 저장
            prof.save()

            # 저장 후, 자신의 프로필 페이지로 리다이렉트
            # (accounts:profile → urls.py의 name="profile" 경로)
            return redirect("accounts:profile")

    # GET 요청(즉, 페이지 첫 방문 또는 리다이렉트 후 재접속)일 때
    else:
        # 기존 기본역을 폼의 초기값으로 세팅
        form = ProfileForm(initial={
            "preferred_station_1": prof.preferred_station_1,
            "preferred_station_2": prof.preferred_station_2,
            "preferred_station_3": prof.preferred_station_3,
        })

    # arrivals/base.html 템플릿을 렌더링
    # 'content_for_profile': True는 base.html 안에서 프로필 전용 블록을 표시하기 위한 플래그로 사용됨
    return render(request, "arrivals/base.html", {
        "form": form,
        "content_for_profile": True,  # base 템플릿 재사용 목적의 조건 플래그
    })
