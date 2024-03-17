"""recipeexchange URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("recipes.urls"), name="recipes-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
]
