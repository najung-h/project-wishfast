from django import forms


class ProfileForm(forms.Form):
    """
    사용자의 선호역 3개를 입력받기 위한 폼입니다.
    """
    preferred_station_1 = forms.CharField(
        label="선호역 1",
        required=False,  # 필수가 아님
        widget=forms.TextInput(attrs={"placeholder": "예) 신도림", "class": "input"})
    )
    preferred_station_2 = forms.CharField(
        label="선호역 2",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "예) 강남", "class": "input"})
    )
    preferred_station_3 = forms.CharField(
        label="선호역 3",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "예) 홍대입구", "class": "input"})
    )