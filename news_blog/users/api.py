from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from django.contrib.auth import login
from users.serializers import UserRegistrationSerializer, UserLoginSerializer, CustomUserSerializer


class UserRegistrationAPIView(GenericAPIView):
    """
    API для создания нового пользователя.
    """
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(f'Пользователь {request.data["username"]} успешно зарегистрирован',
                        status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    API для аутентификации существующего пользователя, и получения токена.
    """
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        token = RefreshToken.for_user(user)
        data = CustomUserSerializer(user).data
        data['tokens'] = {'refresh': str(token), 'access': str(token.access_token)}
        login(request, user)
        return Response(data, status=status.HTTP_200_OK)
