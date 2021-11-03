from django.test import TestCase
from django.contrib.auth.models import User
from watch.models import *

# Create your tests here.


class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='developer',
            password='password'
        )
        self.neighborhood = Neighborhood(
            name='Test Neighbourhood', location=self.location, occupants_count=100, admin_id=self.admin.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood, Neighborhood))

    def test_save_method(self):
        self.neighbourhood.create_neigborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_method(self):
        self.neighborhood.create_neigborhood()
        self.neighborhood.delete()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)


class PostTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='dev-kev',
            password='password'
        )
        self.post = Post(title='Test Post', content='Test Content',
                         location=self.location, category=self.category, user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_method(self):
        self.post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.save()
        self.post.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)
