from django.shortcuts import render
from django.views.generic import ListView,View

from newsread.models import Article, NewsSource

class NewsSourceView(ListView):
    model = NewsSource
    template_name = "show_image.html"
    page_title = "News Source"

# Create your views here.
