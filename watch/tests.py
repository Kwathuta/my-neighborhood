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
