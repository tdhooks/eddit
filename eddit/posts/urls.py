from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.focus, name='focus'),
    path('post/', views.post, name='post'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
]
