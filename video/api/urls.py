from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('videos/', views.getVideos),
    path('add/', views.addVideo),
    path('delete/<str:pk>/', views.deleteVideo),
]