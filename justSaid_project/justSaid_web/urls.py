from django.urls import path
from .views import AddPostView, HomeView, BlogDetailView

urlpatterns = [
    path('', HomeView.as_view(),name='home' ),
    path('blog/<int:pk>', BlogDetailView.as_view(),name='blog-detail'), # pk=primary key
    path('add_post/',AddPostView.as_view(),name='add_post')
    
]
