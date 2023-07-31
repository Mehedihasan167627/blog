from django.urls import path 

from .views import*

urlpatterns=[
    path("",HomeAPIView.as_view())
]