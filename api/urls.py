from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"), #class based view
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestory.as_view(), name="update"),
    path("blogpost/get/", views.BlogPostList.as_view(), name="get"),
    path("person/", views.index, name="person")
]