from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blogcore'

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('blog/tag/<slug:tag_slug>', views.post_list, name='post_list_tag'),
    path('blog/<slug:post>/', views.post_detail, name='post_detail'),
    path('mail/<slug:post>/', views.post_share, name='post_share'),
    path('comment/<slug:post>/', views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
