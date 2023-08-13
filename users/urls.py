from django.urls import path 
from .views import*
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/",RegisterAPIView.as_view()),
    path("profile/",RegisterAPIView.as_view()),
 
]


