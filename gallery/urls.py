from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/ajouter/', views.add_photo, name='add_photo'),
    path('video/ajouter/', views.add_video, name='add_video'),
    path('photo/<slug:slug>/', views.photo_detail, name='photo_detail'),
    path('video/<slug:slug>/', views.video_detail, name='video_detail'),
    path('photo/supprimer/<slug:slug>/', views.delete_photo, name='delete_photo'),
    path('video/supprimer/<slug:slug>/', views.delete_video, name='delete_video'),
]
