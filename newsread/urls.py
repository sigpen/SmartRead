from django.conf.urls import url


from newsread import views

appname = 'newsread'
urlpatterns = [
    url(r'^images/?P<image>?P$', views.NewsSourceView.as_view()),
    url(r'^article$', views.ArticleView.as_view(), name="article"),
    url(r'^source$', views.NewsSourceView.as_view(), name="news_source"),
    # url(r'^base$', views.BaseView.as_view(), name="base"),

    # url(r'^$', views.CategoryView.as_view(), name="Category"),
    # url(r'^$', views.ArticleView.as_view(), name="Article"),
]