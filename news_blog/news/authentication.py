from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request

from users.models import CustomUser


class CustomAuth(BaseAuthentication):
    """Проверка пользователя на аутентификацию при попытке POST запроса"""
    def authenticate(self, request: Request):
        username = getattr(request._request, 'user', None)

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('Пользователь не авторизован')

        if user.is_active:
            return user, None
        else:
            return exceptions.AuthenticationFailed('Пользователь не активен')
