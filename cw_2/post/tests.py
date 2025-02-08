from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Test Title", description="Test Description", author="Test Author")

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test Title')
        self.assertEqual(post.description, 'Test Description')
        self.assertEqual(post.author, 'Test Author')