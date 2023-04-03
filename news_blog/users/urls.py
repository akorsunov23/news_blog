from django.urls import path
from users.api import UserRegistrationAPIView, UserLoginAPIView

app_name = 'user'

urlpatterns = [
	path('register/', UserRegistrationAPIView.as_view(), name='create_user'),
	path('login/', UserLoginAPIView.as_view(), name='login_user'),
]
