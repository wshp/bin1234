from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('post/delete/<int:id>/', views.post_delete, name='post_delete'),
]
