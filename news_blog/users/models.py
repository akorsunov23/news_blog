from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

class CustomUser(AbstractUser):
	objects = CustomUserManager()

	USERNAME_FIELD = 'username'




