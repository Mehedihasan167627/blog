from django.urls import path 
from .views import*

urlpatterns=[
    path("right-sidebar/",SidebarView.as_view()),
    path("home/",HomeAPIView.as_view()),
    path("posts/",PostListView.as_view()),
    path("post/<slug:slug>/",PostDetailAPIView.as_view()),
]