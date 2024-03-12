""" Importing the models and registering them with the admin interface. """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Comment, Post, Profile


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Custom admin interface for the Post model. """
    list_display = ('title', 'slug', 'status',
                    'created_on', 'get_category_title')
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
        """ Display the title of the category. """
        return obj.category.title if obj.category else ''

    get_category_title.short_description = 'Category'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Custom admin interface for the Comment model """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        """ Action to approve selected comments. """
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Custom admin interface for the Category model. """
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Custom admin interface for the Profile model. """
    list_display = ('user', 'profile_picture')
    search_fields = ('user', 'profile_picture')
