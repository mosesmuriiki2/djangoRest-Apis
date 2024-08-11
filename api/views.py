from django.shortcuts import render

from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    #overide the existing generic methods 
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self, request, format=None):
        #Get the blogs title if none return a empty string
        title = request.query_params.get("title", "No data")
        
        if title:
            #filter the queryset based on the title
            blog_post = BlogPost.objects.filter(title__icontains= title)
        else:
            #if no title is provided return aLL BLOG post
            blog_post = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)