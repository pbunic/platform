from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from mdeditor.fields import MDTextField
from taggit.managers import TaggableManager


class Info(models.Model):
    """Site-related static informations."""
    base_title = models.CharField(max_length=30, help_text='Navigation spot title.')
    home_title = models.CharField(max_length=50, help_text='Browser tab and huge landing page title.')
    home_paragraph = models.TextField(max_length=500, help_text='Landing page short web introduction.')
    about_blog = models.TextField(max_length=2500, help_text='Blog vision and roadmap.')
    about_author = models.TextField(max_length=2500, help_text='Some personal informations.')
    contact_email = models.EmailField(help_text='Email for contact.')
    instagram_feed = models.TextField(max_length=2500, blank=True, help_text='Instagram embeded code.')
    copyright = models.CharField(max_length=100, blank=True, help_text='Bottom copyright text.')

    class Meta:
        verbose_name_plural = 'Informations'

    def __str__(self):
        return 'Website main informations'


class Footer(models.Model):
    """Footer links."""

    class Section(models.TextChoices):
        """Footer links grouping."""
        WEBSITE = 'WL', 'Website links'
        OTHER = 'OL', 'Other links'
        SOCIAL = 'SL', 'Social links'

    link_name = models.CharField(max_length=50)
    link_slug = models.SlugField(max_length=200, unique=True)
    link_section = models.CharField(max_length=2, choices=Section.choices)
    template_title = models.CharField(max_length=100)
    template_body = MDTextField()

    class Meta:
        verbose_name_plural = 'Footer links'
        ordering = ['link_section']
        indexes = [
            models.Index(fields=['link_section']),
        ]

    def __str__(self):
        return self.link_name

    def get_absolute_url(self):
        return reverse('blog:general_info', args=[self.link_slug])


class Newsletter(models.Model):
    """Website subscriptions to the newsletters."""
    email = models.EmailField()
    active = models.BooleanField(default=True)
    subscribed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Subscriptions'
        ordering = ['-subscribed']
        indexes = [
            models.Index(fields=['-subscribed']),
        ]

    def __str__(self):
        return self.email


class TechStack(models.Model):
    """Professional working stack."""
    name = models.CharField(max_length=30, help_text='Name of technology.')
    icon = models.ImageField(upload_to='techstack/', help_text='Logo icon.')
    description = models.TextField(max_length=300, help_text='Just core description of service-related usage.')
    url = models.URLField(max_length=150, help_text='Website of the technology.')
    show = models.BooleanField(default=True, help_text='Should be rendered?')

    class Meta:
        verbose_name_plural = 'Techstack'
        ordering = ['show']
        indexes = [
            models.Index(fields=['show']),
        ]

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    """Custom manager for filtering published posts."""
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Post publishing."""

    class Status(models.TextChoices):
        """Post status."""
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        ARCHIVED = 'AR', 'Archived'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    imagecover = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    body = MDTextField()
    tags = TaggableManager(
        verbose_name=_('Tags'),
        help_text=_('A comma-separated tags. '
                    'Use quotes for multiple words '
                    'and lowercase letters.')
    )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # Managers
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
