from django.urls import path
from . import views

urlpatterns = [
    # URL for the starting page, mapped to StartingPageView
    path('', views.StartingPageView.as_view(), name="starting-page"),

    # URL for displaying all posts, mapped to AllPostsView
    path('posts/', views.AllPostsView.as_view(), name="posts-page"),

    # URL for displaying a single post, mapped to SinglePostView
    # <slug:slug> captures a post's slug in the URL
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name="post-detail-page"),

    # URL for the "Read Later" feature, mapped to ReadLaterView
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]

