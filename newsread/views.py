from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,View

from newsread.models import Article, NewsSource


class NewsSourceView(ListView):
    model = NewsSource
    page_title = "News Source"

# class CategoryView(ListView):
#     model = Category
#

# class ArticleView(ListView):
#     model = Article
#

class IndexView(ListView):
    source = NewsSource.objects.all()
    article = Article.objects.all()

