from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views.generic import ListView, View

from newsread.models import Article, NewsSource, Category


class NewsSourceView(ListView):
    model = NewsSource
    template_name = "news_source.html"
    page_title = "News Source"


class ArticleView(ListView):
    model = Article
    template_name = "news_source.html"
    page_title = "Article"


class CustomListView(ListView):
    model = Article
    template_name = "custom.html"

    def get_queryset(self):
        x = self.kwargs['cat']
        return Article.objects.filter(category__title=x).all()

