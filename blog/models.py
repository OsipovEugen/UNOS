from time import time

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


def gen_slug(slug):
    new_slug = slugify(slug, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    # TODO: 'add rubrick, comments and likes'
    title = models.CharField(max_length=150, null=False)
    body = models.TextField(blank=True)
    images = models.ImageField(blank=True, upload_to='post_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # rubrick = models.ForeignKey(Rubrick, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'title {self.title}, Slug {self.slug}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog_delete', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update', kwargs={'slug': self.slug})

