""" App Admin Models """
from django.contrib import admin
from .models import Member, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Member)
class MemberAdmin(SummernoteModelAdmin):
    """
    This class displays a summernote model and  a nice list filter
    """
    list_display = ('title', 'slug', 'status', 'created_on', 'user_email')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('blurb',)
    actions = ['approve_member']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    This class displays admin model shown in the admin panel
        for the admin
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']  # displays approve comments

    def approve_comments(self, request, queryset):
        """ Comments to be approved """
        queryset.update(approved=True)
