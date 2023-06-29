import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User
from .mixins import GetSubscribedMixin


class TokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label='Электронная почта',
        write_only=True)
    password = serializers.CharField(
        label='Пароль',
        trim_whitespace=False,
        write_only=True,
        style={'input_type': 'password'}, )
    token = serializers.CharField(
        label='Токен',
        read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                email=email,
                password=password)
            if not user:
                raise serializers.ValidationError(
                    'Неверно введен логин пользователя и/или пароль.',
                    code='authorization')
        else:
            raise serializers.ValidationError(
                'Введите адрес электронной почты и пароль.',
                code='authorization')
        attrs['user'] = user
        return attrs


class ListUserSerializer(GetSubscribedMixin, serializers.ModelSerializer):
    is_subscribed = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'is_subscribed')


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name',
            'last_name', 'email', 'password',)

    def validate_password(self, password):
        validators.validate_password(password)
        return password


class PasswordUserSerializer(serializers.Serializer):
    password = serializers.CharField(
        label='Текущий пароль')
    new_password = serializers.CharField(
        label='Новый пароль')

    def validate_password(self, password):
        user = self.context['request'].user
        if not authenticate(
                username=user.email,
                password=password):
            raise serializers.ValidationError(
                'Неверно введен логин пользователя и/или пароль.',
                code='authorization')
        return password

    def validate_new_password(self, new_password):
        validators.validate_password(new_password)
        return new_password

    def create(self, validated_data):
        password = make_password(
            validated_data.get('new_password'))
        user = self.context['request'].user
        user.password = password
        user.save()
        return validated_data
