from django.urls import path
from . import views

urlpatterns = [
    path('post/create/', views.post_create, name='post_create'),
]
