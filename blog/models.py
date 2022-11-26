from django.db import models
from uuid import uuid5, NAMESPACE_URL
from django.utils.translation import gettext_lazy as _
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings


class Article(models.Model):

    def article_dir(self, filename: str) -> str:
        return f'{uuid5(NAMESPACE_URL, str(self.id))}/{filename}'

    class StatusChoices(models.IntegerChoices):
        published = 1, _('published')
        queue = 2, _('queue')
        draft = 3, _('draft')

    title = models.CharField(max_length=720)
    slug = models.SlugField(max_length=1200, blank=True)
    header = models.CharField(max_length=310, blank=True)
    image = ProcessedImageField(upload_to=article_dir, max_length=255, default='default/img.jpg',
                                processors=[ResizeToFill(500, 500)], format='JPEG', options={'quality': 50})
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_articles', on_delete=models.CASCADE)
    body = models.TextField()
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.draft)
    tags = models.ManyToManyField('Tags', related_name='tags_article')

    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article_detail", args=(self.id, self.slug))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
            self.header = self.body[:310]
        return super().save(*args, **kwargs)


class Tags(models.Model):
    name = models.CharField(max_length=60, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Comments(models.Model):
    content = models.CharField(max_length=500)
    sub_comment_id = models.ForeignKey('self', related_name='sub_comments', null=True, blank=True,
                                       on_delete=models.CASCADE)

    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_comments', on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, related_name='article_comments', on_delete=models.CASCADE)

    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    is_sub = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.content
