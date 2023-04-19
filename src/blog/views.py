from django.shortcuts import render

from blog import models


def view_posts(request):
    posts = models.Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)
