from django.conf.urls import url

from newsread import views

appname = 'newsread'
urlpatterns = [
    url(r'^images/?P<image>?P$', views.NewsSourceView.as_view()),
    url(r'^$', views.NewsSourceView.as_view(), name="news_source"),
    # url(r'^$', views.CategoryView.as_view(), name="Category"),
    # url(r'^$', views.ArticleView.as_view(), name="Article"),
]