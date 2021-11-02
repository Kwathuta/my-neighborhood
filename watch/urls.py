from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("profile/", views.profile, name="profile"),
    path('profile/update', views.update_profile, name='update_profile'),
    path('posts', views.posts, name='posts')
]
