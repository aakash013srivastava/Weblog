from .models import Article
from django.shortcuts import render,get_object_or_404
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    return render(request,'article/index.html',{'articles':articles})

def detail(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
    return render(request,'article/detail.html',{'article':article})

def new(request):
    form = ArticleForm()
    return render(request,'article/new.html',{'form':form})

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            new_article = Article()
            new_article.title = title
            new_article.content = content
            new_article.author = "Aakash"
            new_article.save()
    else:
        form = ArticleForm()

    return render(request,'article/new.html',{'form':form})
