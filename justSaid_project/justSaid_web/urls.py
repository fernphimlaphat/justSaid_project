from django.urls import path
from .views import AddPostView, HomeView, BlogDetailView, UpdatePostView,DeletePostView,AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(),name='home' ),
    path('blog/<int:pk>', BlogDetailView.as_view(),name='blog-detail'), # pk=primary key
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('blog/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('blog/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
]
