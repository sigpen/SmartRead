from django.conf.urls import url


from newsread import views, models

appname = 'newsread'
urlpatterns = [
    url(r'^images/?P<image>?P$', views.NewsSourceView.as_view()),
    url(r'^article$', views.ArticleView.as_view(), name="article"),
    url(r'^source/$', views.NewsSourceView.as_view(), name="news_source"),
    url(r'^source/(?P<cat>\w+)$', views.CustomListView.as_view(), name="category"),
]