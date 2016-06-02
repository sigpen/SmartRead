from django.shortcuts import render
from django.views.generic import ListView,View

from newsread.models import Article, NewsSource


    # so = NewsSource.objects.all()
    # ar = Article.objects.all()


    # def get_context_data(self, **kwargs):
    #     context = super(BaseView, self).get_context_data(**kwargs)
    #    for article in Base.objects.all():
    #        x = Article.objects.all()



class NewsSourceView(ListView):
    model = NewsSource
    template_name = "news_source.html"
    page_title = "News Source"



class ArticleView(ListView):
    model = Article
    template_name = "article.html"
    page_title = "Article"
#



# Create your views here.
