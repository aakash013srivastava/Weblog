from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
    # /article/
    path('',views.index,name='index'),
    #/article/71
    url(r'^(?P<article_id>[0-9]+)/$',views.detail,name='detail'),

    url(r'^new/$',views.new,name='new'),
    url(r'^create/$',views.create,name='create'),
]
