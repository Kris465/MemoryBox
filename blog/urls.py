
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('main/', views.BlogListView.as_view(), name='main'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('add_post/', views.AddPostApiView.as_view(), name='add_post_api'),
]
