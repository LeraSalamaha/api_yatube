from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404

from posts.models import Comment, Group, Post
from .mixins import AuthorPermissionMixin
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(AuthorPermissionMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(AuthorPermissionMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_pk']
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)
