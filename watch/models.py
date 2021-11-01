from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create_neigborhood(self):
        self.save()

    def delete(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        neighborhood = cls.objects.filter(pk=neighborhood_id)
        return neighborhood

    @classmethod
    def update_neighborhood(cls, pk):
        cls.objects.filter(pk=pk).update()

    def update_occupants(self):
        pass


class user_profile(models.Model):
    name = models.CharField(max_length=200)
    neighborhood = models.OneToOneField(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)


class Business():
    name = models.CharField(max_length=200)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.filter(pk=business_id)
        return business

    @classmethod
    def update_business(cls, pk):
        cls.objects.filter(pk=pk).update()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def search_by_title(cls, search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post
