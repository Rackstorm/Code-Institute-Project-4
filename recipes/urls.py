from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/saved-posts/', views.saved_recipes, name='saved_posts'),
    path('profile/liked-posts/', views.liked_recipes, name='liked_posts'),
]
