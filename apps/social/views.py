from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import *
from rest_framework import filters
from rest_framework import permissions
class UserProfileViewSets(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
class FollowViewSets(viewsets.ModelViewSet):
	queryset = Follow.objects.all()
	serializer_class = FollowSerializer
class PostViewSets(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['hashtag',]
	search_fields = ['user']
class PostLikeViewSets(viewsets.ModelViewSet):
	queryset = PostLike.objects.all()
	serializer_class = PostLikeSerializer
class CommentViewSets(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
class CommentLikeViewSets(viewsets.ModelViewSet):
	queryset = CommentLike.objects.all()
	serializer_class = CommentLikeSerializer
class StoryViewSets(viewsets.ModelViewSet):
	queryset = Story.objects.all()
	serializer_class = StorySerializer
class GroupViewSets(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
