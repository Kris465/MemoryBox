from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.all()  # Получаем все статьи
    return render(request, 'blog/article_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})
