from rest_framework import routers
from posts.views.views import PostViewSet

router = routers.DefaultRouter()
router.register(prefix='posts', basename='posts', viewset=PostViewSet)

