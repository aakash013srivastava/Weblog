from .models import Article,Comment
from django.shortcuts import render,get_object_or_404,redirect
from .forms import ArticleForm,CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login



def index(request):
    articles = Article.objects.all()
    return render(request,'article/index.html',{'articles':articles})

def detail(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
    comment_form = CommentForm()
    return render(request,'article/detail.html',{'article':article,'comment_form':comment_form})

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
            articles = Article.objects.all()
            return render(request,'article/index.html',{'articles':articles})
    else:
        form = ArticleForm()
        return render(request,'article/new.html',{'form':form})

def post_comment(request,article_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_text = comment_form.cleaned_data['comment_text']
            comment = Comment()
            comment.comment_text = comment_text
            comment.comment_author = "Aakash"
            comment.article = Article.objects.get(pk=article_id)
            comment.save()
    else:
        comment_form = CommentForm()

    return render(request,'article/detail.html',{'comment_form':comment_form})

def signup(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            #user = authenticate(username=username,password=raw_password)
            #login(request,user)
            #return redirect('article/login')
            return render(request,'article/login.html')
    else:
        form = UserCreationForm()

    return render(request,'article/signup.html',{'form':form})

