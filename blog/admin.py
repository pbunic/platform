from django.contrib import admin
from django.db import models
from django.forms import TextInput

from .models import (
    Info,
    Footer,
    Newsletter,
    TechStack,
    Post,
    HomeLab,
)


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['base_title']

    def has_add_permission(self, request):
        # Restrict object add if already exists
        if not Info.objects.exists():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        # Restrict delete
        return False

    def save_model(self, request, obj, form, change):
        # Database model update
        if not Info.objects.exists():
            obj.save()
        else:
            info_instance = Info.objects.first()
            info_instance.base_title = obj.base_title
            info_instance.home_title = obj.home_title
            info_instance.home_paragraph = obj.home_paragraph
            info_instance.about_blog = obj.about_blog
            info_instance.about_author = obj.about_author
            info_instance.contact_email = obj.contact_email
            info_instance.copyright = obj.copyright
            info_instance.save()


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['link_name', 'link_slug', 'link_section']
    list_filter = ['link_section']
    search_fields = ['link_section', 'link_name']
    prepopulated_fields = {'link_slug': ('link_name',)}
    ordering = ['-link_section']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'active', 'subscribed']
    list_filter = ['active', 'subscribed']
    search_fields = ['email']
    date_hierarchy = 'subscribed'
    ordering = ['-subscribed']


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'url']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['id']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'publish']
    list_filter = ['status', 'created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['-status', '-publish']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '72'})},
    }


@admin.register(HomeLab)
class HomeLabAdmin(admin.ModelAdmin):
    list_display = ['title']

    def has_add_permission(self, request):
        # Restrict object add if already exists
        if not HomeLab.objects.exists():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        # Restrict delete
        return False

    def save_model(self, request, obj, form, change):
        # Database model update
        if not HomeLab.objects.exists():
            obj.save()
        else:
            lab_instance = HomeLab.objects.first()
            lab_instance.title = obj.title
            lab_instance.body = obj.body
            lab_instance.save()
