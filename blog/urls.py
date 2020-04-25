# blog/urls.py
"""This is the url route for app 'blog''"""
from django.urls import path
from blog import views
app_name = 'blog'

urlpatterns = [
    # path('', views.HomeTemplateView.as_view(), name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('post/<slug:slug>/<uuid:uuid>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/tag/<slug:slug>/', views.PostByTagListView.as_view(), name='post_list_with_tag'),
]