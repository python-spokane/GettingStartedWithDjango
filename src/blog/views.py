from django.shortcuts import render

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse

from blog import models


def list_posts(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        ...

    posts: QuerySet[models.Post] = models.Post.objects.all()
    return render(
        request,
        "blog/list_posts.html",
        context={"posts": posts},
    )
