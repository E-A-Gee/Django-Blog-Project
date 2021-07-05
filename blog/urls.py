from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    BatmanView,
    SupermanView,
    SpidermanView,
    FlashView,

)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


    path('search_posts/', views.search_posts, name='search-posts'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('batman/', BatmanView.as_view(), name='batman-posts'),
    path('superman/', SupermanView.as_view(), name='superman-posts'),
    path('spiderman/', SpidermanView.as_view(), name='spiderman-posts'),
    path('flash/', FlashView.as_view(), name='flash-posts'),

    path('about/', views.about, name='blog-about'),
]