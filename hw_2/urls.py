from django.contrib import admin
from django.urls import path
from movie import views as movie_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movie_views.movie_list, name='movie_list'),
    path('movies/<int:id>/', movie_views.movie_detail, name='movie_detail'),
    path('articles/', blog_views.article_list, name='article_list'),
    path('articles/<int:id>/', blog_views.article_detail, name='article_detail'),
    path('api/movies/', movie_views.api_movie_list, name='api_movie_list'),
    path('api/movies/<int:id>/', movie_views.api_movie_detail, name='api_movie_detail'),
    path('api/articles/', blog_views.api_article_list, name='api_article_list'),
    path('api/articles/<int:id>/', blog_views.api_article_detail, name='api_article_detail'),
]
