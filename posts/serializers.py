from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
        )
        model = Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 
            'get_full_name',
            'username',
            'email',
            'date_joined',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',

            
        )