app_name = "blog"

from django.urls import path
from blog import views

urlpatterns = [
    path("", views.view_posts, name="view_posts"),
]
