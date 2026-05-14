from rest_framework import serializers
from .models import Article


# 단일 게시글 데이터(단일 인스턴스)를 직렬화 하는 도구
# 그러면 ArticleSerializer를 단일 게시글에서 못함?
# => 놉. 
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

# 전체 게시글 데이터(쿼리 셋)을 직렬화하는 도구
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )