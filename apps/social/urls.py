from django.urls import path,include,re_path
from .views import *
urlpatterns = [
	 path('accounts/', include('allauth.urls')),
	 path('userprofile/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='userprofile_list'),
	 path('userprofile/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='userprofile_detail'),
	 path('follow/', FollowViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='follow_list'),
	 path('follow/<int:pk>/', FollowViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='follow_detail'),
	 path('post/', PostViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='post_list'),
	 path('post/<int:pk>/', PostViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='post_detail'),
	 path('postlike/', PostLikeViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='postlike_list'),
	 path('postlike/<int:pk>/', PostLikeViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='postlike_detail'),
	 path('comment/', CommentViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='comment_list'),
	 path('comment/<int:pk>/', CommentViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='comment_detail'),
	 path('commentlike/', CommentLikeViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='commentlike_list'),
	 path('commentlike/<int:pk>/', CommentLikeViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='commentlike_detail'),
	 path('story/', StoryViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='story_list'),
	 path('story/<int:pk>/', StoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='story_detail'),
	 path('group/', GroupViewSets.as_view({'get': 'list', 'post': 'create'}),
		name='group_list'),
	 path('group/<int:pk>/', GroupViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
		name='group_detail'),
]