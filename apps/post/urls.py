from django.urls import path

from apps.post.views import PostsView, PostCreateView, PostView


urlpatterns = [
    path("", PostsView.as_view(), name="index_post"),
    path("<int:id>", PostView.as_view(), name="post"),
    path("crear", PostCreateView.as_view(), name="crear_post"),
]
