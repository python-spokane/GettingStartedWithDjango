from django.db import models

from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=512)


class Post(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=512)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_created=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    publish_date = models.DateTimeField(auto_created=True)
