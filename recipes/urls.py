""" This module defines the URL patterns for the recipes app. """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.PostSearch.as_view(), name='post_search'),
    path('profile/', views.ProfileView, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('create/', views.PostCreateView, name='post_create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/like/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
]
