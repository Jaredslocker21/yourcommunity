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
    

# Register your models here.
