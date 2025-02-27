from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

# Создаем вложенный роутер для комментариев
posts_router = routers.NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = router.urls + posts_router.urls

# Добавьте этот путь для токена аутентификации
urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
