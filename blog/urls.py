from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog.views import PostListView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog_list'),
    path('blog/post_create', PostCreateView.as_view(), name='post_create'),
    path('blog/post_update/<str:slug>', PostUpdateView.as_view(), name='post_update'),
    path('blog/<str:slug>', PostDetailView.as_view(), name='blog_detail'),
    path('blog/<str:slug>/delete', PostDeleteView.as_view(), name='blog_delete'),


]
