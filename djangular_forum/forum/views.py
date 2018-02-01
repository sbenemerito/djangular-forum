from rest_framework.viewsets import ModelViewSet

from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD on Post model
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class CommentViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD on Comment model
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save()
