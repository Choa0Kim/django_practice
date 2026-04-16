# django Form
# 1. 기본적인 유효성 검증을 자동으로 해준다.
# 2. 사용자 입력을 편하게 받을 수 있다.

from django import forms
# From: 모델과 연관없는 데이터도 입력 가능하다.
#DB 저장 기능 X -> 직접 저장ㅎ하는 기능을 구현해야 함 
class ArticleFormExample(forms.Form):
    # - 입력 받는 필드를 직접 정의해주어야 한다.
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    is_public = forms.BooleanField()


from .models import Article

# ModelForm: models.py 에 정의된 필드만 입력 받겠다.
# - 모델의 필드와 매핑이 가능하다.
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields: tuple이나 list로 작성
        fields = ("title", "content", "is_public", )
        labels = {
            'title': "제목",
            "content": "내용",
            'is_public': "공개여부"
        }

        error_meaages = {
            "title": {
                "required": "제목은 필수 입력입니다."
            },
            "content": {
                "required": "내용은 필수 입력입니다."
            }
        }