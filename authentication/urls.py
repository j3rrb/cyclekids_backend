from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from authentication.views import RegisterView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('register/', RegisterView.as_view(), name='register')
]
