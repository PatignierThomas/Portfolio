from django.urls import path

from blog.views import BlogHome, BlogPostCreate, BlogPostEdit, BlogPostDetail, BlogPostDelete

app_name = "myblog"

urlpatterns = [
    path('', BlogHome.as_view(), name="blog"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    path('<slug:slug>/', BlogPostDetail.as_view(), name="post"),
    path('edit/<slug:slug>/', BlogPostEdit.as_view(), name="edit"),
    path('delete/<slug:slug>/', BlogPostDelete.as_view(), name="delete"),

    ]


