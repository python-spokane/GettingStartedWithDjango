from django.db import models
from django.utils import timezone


class Post(models.Model):
    """A blog post."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField("Tag", related_name="posts")

    def __str__(self):
        return self.title


class Tag(models.Model):
    """A tag for a blog post."""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """A comment on a blog post."""

    author = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.author} on {self.post}"
