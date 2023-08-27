from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_queryset(self):
        return Post.objects.all()

class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class APIHone(TemplateView):
    template_name = 'api_home.html'


