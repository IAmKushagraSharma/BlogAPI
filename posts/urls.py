from django.urls import path, include
from rest_framework.routers import SimpleRouter


from .views import *


router = SimpleRouter()
router.register('users', UsersViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = router.urls

