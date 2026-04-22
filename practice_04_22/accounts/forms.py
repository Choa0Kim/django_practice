from django.contrib.auth.forms import UserCreationForm

# 프로젝트가 바라보고있는 User 모델을 가져와라
from django.contrib.auth import get_user_model

# 회원가입 시에 활용할 Form
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'nickname',
            'email',
            'profile_image',
        )

