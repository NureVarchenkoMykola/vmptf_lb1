from django.shortcuts import render, get_object_or_404
from .models import Article

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/article_list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article
    }
    return render(request, 'articles/article_detail.html', context)

@api_view(['GET'])
def article_api_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)