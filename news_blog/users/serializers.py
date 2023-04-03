from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
	"""
	Сериализатор модели CustomUser.
	"""
	class Meta:
		model = CustomUser
		fields = ('id', 'username',)

class UserRegistrationSerializer(serializers.ModelSerializer):
	"""
	Сериализатор запросов на регистрацию и создания нового пользователя.
	"""

	class Meta:
		model = CustomUser
		fields = ('username', 'password', 'is_superuser')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		if validated_data['is_superuser']:
			return CustomUser.objects.create_superuser(**validated_data)
		return CustomUser.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
	"""
	Класс Serializer для аутентификации пользователей по username и паролю.
	"""
	username = serializers.CharField(max_length=255, write_only=True)
	password = serializers.CharField(max_length=128, write_only=True)

	def validate(self, data):
		user = authenticate(**data)

		if user is None:
			raise serializers.ValidationError('Пользователь не найден, проверьте введённые данные')

		if not user.is_active:
			raise serializers.ValidationError('Пользователь неактивен')

		return user
