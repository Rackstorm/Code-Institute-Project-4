from django.contrib import admin
from .models import Post, Comment, Category, Profile
from django_summernote.admin import SummernoteModelAdmin


# Registering the Post model with a custom admin interface
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'get_category_title')
    search_fields = ['title', 'content', 'category__title']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'category', 'featured_image', 'excerpt', 'content', 'status', 'likes'),
        }),
    )

    readonly_fields = ('slug',)

    def get_category_title(self, obj):
        return obj.category.title if obj.category else ''

    get_category_title.short_description = 'Category'


# Registering the Comment model with a custom admin interface
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# Registering the Category model with a custom admin interface
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


# Registering the Profile model with a custom admin interface
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user', 'profile_picture')
