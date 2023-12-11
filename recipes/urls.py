from . import views
from django.urls import path
from .views import CustomSignupView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.PostSearch.as_view(), name='post_search'),
    path('profile/', views.ProfileView, name='profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/like/', views.PostLike.as_view(), name='post_like'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('signup/', CustomSignupView.as_view(), name='account_signup'),

]
