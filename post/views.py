from post.models import Posts
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from post.serializers import PostSerializer


class PostsList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        print(self)
        return Posts.objects.all()
