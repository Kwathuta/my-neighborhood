from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("profile/update", views.update_profile, name="update_profile"),
    path("posts", views.posts, name='posts'),
    path("post/add/", views.new_post, name="add_post"),
    path("business/add/", views.new_business, name="new_business"),
    path("contact/add/", views.new_contact, name="new_contact"),
    path("businesses/", views.businesses, name="business"),
    path("contacts/", views.contacts, name="contacts"),
]
