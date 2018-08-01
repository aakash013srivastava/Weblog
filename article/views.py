from django.http import Http404
from .models import Article
from django.shortcuts import render


def index(request):
    articles = Article.objects.all()
    return render(request,'article/index.html',{'articles':articles})

def detail(request,article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404('Article does not exist')
    return render(request,'article/detail.html',{'articles':article})


