from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)  #forms에서 제공하는 텍스트창(좀 더 넓은 칸)으로 설정

class ArticleForm(forms.ModelForm):
    class Meta:  #model, field 정보를 넣어주는게 필수
        model = Article
        fields= ['title', ] # 사용자의 입력으로 받을 필드를 설정. 리스트로 추천, 튜플의 경우 ,도 필요.
        #  단일요소가 불가하기 떄문. ('title', )
        fields = '__all__' # 전체 필드를 입력으로 받을 때 사용하는 설정

