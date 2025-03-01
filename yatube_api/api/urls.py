from django.urls import path, re_path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = router.urls

urlpatterns += [
    re_path(
        r'^posts/(?P<post_pk>[^/.]+)/comments/$',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post-comments-list'
    ),
    re_path(
        r'^posts/(?P<post_pk>[^/.]+)/comments/(?P<pk>[^/.]+)/$',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='post-comments-detail'
    ),
]

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
