from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )

        cls.post = Post.objects.create(
            author= cls.user,
            title = 'Test title',
            body = 'Test body',
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'Test title')
        self.assertEqual(self.post.body, 'Test body')
        self.assertEqual(str(self.post), 'Test title')
        