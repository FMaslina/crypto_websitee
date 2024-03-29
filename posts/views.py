from rest_framework import generics, status
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer


class PostGetView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        post = self.queryset.get(pk=kwargs['pk'])
        lang = request.GET['lang']
        serialized_post = self.serializer_class(post, context={'lang': lang, 'request': request}).data

        return Response(status=status.HTTP_200_OK, data=serialized_post)


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        lang = request.GET['lang']
        serialized_posts = self.serializer_class(self.get_queryset(), context={'lang': lang, 'request': request},
                                                 many=True).data

        return Response(status=status.HTTP_200_OK, data=serialized_posts)
