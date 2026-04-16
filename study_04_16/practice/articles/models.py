from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)  # 0이상의 정수만 가능. 디폴트 값: 0
    is_public = models.BooleanField(default=True)

#  - 제목(title) / 문자열 *& 최대 100글자
#  - 내용(content) / 문자열
#  - 작성시간(created_at) / 시간 & 작성 시 자동 갱신
#  - 수정시간(updated_at) / 시간 & 수정 시 자동 갱신
#  - 조회수(view_count) / 0이상인 정수 & 기본값: 0
#  - 공개여부(is_public) / boolean & 기본값:True

# 앱이름_모델이름 형식으로 테이블 생성됨




