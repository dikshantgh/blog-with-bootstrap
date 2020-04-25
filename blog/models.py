from django.db import models
from django.db.models import Q
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import uuid
from taggit.managers import TaggableManager


class PostManager(models.Manager):
    # returns the post only when the date is not in future and status is published
    def publishable_post(self):
        return self.filter(Q(status='p') & Q(publishable_date__lte=timezone.now()))


# model for all the created posts
class Post(models.Model):
    STATUS_CHOICES = (
        ('p', _('Published')),
        ('d', _('Draft')),
    )
    title = models.CharField(max_length=50, )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    body = models.TextField(verbose_name=_('Content'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publishable_date = models.DateTimeField(default=timezone.now, db_index=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='d', db_index=True)
    # rating =
    dp = models.ImageField(verbose_name='Display Image', upload_to='dp/', null=True)
    tags = TaggableManager()
    slug = models.SlugField(max_length=90, )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug, 'uuid': self.uuid})

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(**kwargs)

    class Meta:
        ordering = ['-publishable_date', ]
        # verbose_name_plural = ''


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    comment_text = models.TextField(verbose_name='Comment')
    commented_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                  related_name='commenter')

    def __str__(self):
        return f'commented by {self.commenter} on post {self.post}'

    class Meta:
        ordering = ['-commented_at']
