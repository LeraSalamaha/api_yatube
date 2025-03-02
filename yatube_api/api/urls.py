from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

router.register(
    r'posts/(?P<post_pk>[^/.]+)/comments',
    CommentViewSet, basename='post-comments'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
